
from flask import render_template, request, redirect, url_for, flash
from python.config import app,db 
from python.models import Department

@app.route('/department',methods=['GET', 'POST'])
def department():
    page = request.args.get('page', 1, type=int)  # Get the current page number, default is 1
    per_page = 5  # Number of records per page

    department_records = Department.query.order_by(Department.id.asc()).paginate(page=page, per_page=per_page)
    return render_template('department.html', department_records=department_records)

@app.route('/useracess',methods=['GET', 'POST'])
def useracess():
    departments = Department.query.all()
    return render_template('user_access_control.html',departments=departments)

@app.route('/add_or_edit_department', methods=['POST'])
def add_or_edit_department():
    department_id = request.form.get('department_id')
    department_name = request.form.get('department_name')

    if department_id:  # Edit mode
        department = Department.query.get(department_id)
        if department:
            department.department_name = department_name
            db.session.commit()
            flash('Department updated successfully!', 'success')
        else:
            flash('Department not found.', 'error')
    else:  # Add mode
        new_role = Department(department_name=department_name)
        db.session.add(new_role)
        db.session.commit()
        flash('Department added successfully!', 'success')

    return redirect(url_for('department'))

@app.route('/delete_department/<int:department_id>', methods=['POST'])
def delete_department(department_id):
    try:
        # Find the statutory record by ID
        department_record = Department.query.get(department_id)
        
        if department_record:
            # Delete all related compliance records
            # Compliance.query.filter_by(statutory_id=statutory_id).delete()
            # Delete the statutory record
            db.session.delete(department_record)
            db.session.commit()
            flash('Department and related compliances deleted successfully!', 'success')
        else:
            flash('Department record not found.', 'error')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting role: {str(e)}', 'error')
    
    return redirect(url_for('department'))