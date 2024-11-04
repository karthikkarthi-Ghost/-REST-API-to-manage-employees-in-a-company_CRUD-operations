from flask import render_template, request, redirect, url_for, flash,jsonify
from python.config import app, db  # Updated import
from python.models import Department, ScreenData


def insert_default_departments():
    if not Department.query.first():  # Check if the table is empty
        default_departments = [
            'Electrical System',
            'Mechanical System',
            'Water and Waste System',
            'Fire Protection System',
            'Building Services and Amenities',
            'Security System'
        ]
        default_departments.sort()
        # Insert each department into the Department table
        for department_name in default_departments:
            new_dept = Department(department_name=department_name)
            db.session.add(new_dept)
        db.session.commit()


from flask import render_template, request, abort
import json


from flask import request, render_template, redirect, url_for, flash
import json

@app.route('/due/', methods=['GET'])
def indexPage():
    try:
        id = request.args.get('id', type=int)
        print('entered', id)

        if id is not None:
            # Edit mode
            screen_data = ScreenData.query.get_or_404(id)
            department = Department.query.get_or_404(screen_data.department_id)
            department_name = department.department_name
            columns = screen_data.columns
            row_data=screen_data.row_data
            tabledataId=id
            
        if id is None:
            # Create mode
            insert_default_departments()
            department_name = request.args.get('department_name', '')
            columns = request.args.get('columns', '[]')
            row_data=request.args.get('row_data','[]')
            tabledataId=id
        # Fetch all departments for dropdown
        departments = Department.query.all()  # Make sure this is not empty
        
        return render_template('due_deligence.html', tabledataId=tabledataId,
                               departments=departments, 
                               department_name=department_name, 
                               screen_name=screen_data.screen_name if id else '', 
                               columns=columns,  
                               row_data=row_data)
        
    except Exception as e:
        app.logger.error(f"Error in due_deligence route: {str(e)}")
        flash("An error occurred while processing your request. Please try again later.", "error")
        return redirect(url_for("due_deligence"))  

@app.route('/edit-table-data', methods=['GET'])
def edit_table_data():
    screen_name = request.args.get('screen_name', None)  
    if screen_name:
        table_data = ScreenData.query.filter_by(screen_name=screen_name).all()
        if not table_data:
            return jsonify({'error': 'No data found for this screen_name'}), 404

        # Prepare data to be sent in the response
        result = {
            'tabledataId':table_data[0].id,
            'department_name': table_data[0].department.department_name,  # Assuming all records are for the same department
            'screen_name': table_data[0].screen_name,
            'columns': table_data[0].columns,
            'row_data': table_data[0].row_data
        }
        # print('result',result);

        return jsonify(result)

    return jsonify({'error': 'screen_name parameter is required'}), 400


@app.route('/submit-table-data', methods=['POST'])
def submit_table_data():
    data = request.json
    print('data is',data)
    screen_name = data.get('screen_name')
    columns = data.get('columns')
    row_data = data.get('row_data')
    department_name = data.get('department_name')
    department_name=department_name.replace('_',' ')

    department = Department.query.filter_by(department_name=department_name).first()
    print('department',department_name)
    if department is None:
        return jsonify({'error': 'Department not found'}, 404)
    
    department_id = department.id
    tabledataId = data.get('tabledataId')  # Get the ID from the request
    print('tableId',tabledataId)
    if tabledataId :
        # Try to find the existing entry by ID
        table_entry = ScreenData.query.get(tabledataId)
        if table_entry:
            # Update the existing entry
            table_entry.screen_name = screen_name
            table_entry.columns = columns
            table_entry.row_data = row_data
            table_entry.department_id = department_id
            db.session.commit()
            return jsonify({'redirect': url_for('view_infrastructure')})
        else:
            return jsonify({'error': 'Entry not found'}, 404)
    else:
        print('entered else')
        # Create a new TableData instance
        table_entry = ScreenData(screen_name=screen_name, columns=columns, row_data=row_data, department_id=department_id)
        print('added new entry')
        # Add and commit to the database
        db.session.add(table_entry)
        db.session.commit()
        return jsonify({'message': 'submission successful'})


from flask import  jsonify, request, abort


@app.route('/get_screen_data/<int:screen_data_id>', methods=['GET'])
def get_screen_data(screen_data_id):
    # Query the ScreenData table by ID
    screen_data = ScreenData.query.get(screen_data_id)
    
    # Check if the record exists
    if not screen_data:
        return jsonify({"error": "ScreenData with the given ID does not exist"}), 404

    # Prepare the data to return in JSON format
    response_data = {
        "id": screen_data.id,
        "screen_name": screen_data.screen_name,
        "columns": screen_data.columns,
        "row_data": screen_data.row_data,
        "department_id": screen_data.department_id,
        "department_name": screen_data.department.department_name  # Assuming department has 'deptname' attribute
    }
    
    return jsonify(response_data), 200

