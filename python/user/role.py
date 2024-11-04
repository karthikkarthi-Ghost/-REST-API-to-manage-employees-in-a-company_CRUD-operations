from flask import render_template, request, redirect, url_for, flash
from python.config import app, db 
from python.models import Department,Role

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('auth-signin.html')

@app.route('/signup_page',methods=['GET', 'POST'])
def some_page():
    return render_template('auth-signup.html')

@app.route('/role',methods=['GET', 'POST'])
def role():
    page = request.args.get('page', 1, type=int)  # Get the current page number, default is 1
    per_page = 5  # Number of records per page
    departments = Department.query.all()
    role_records = Role.query.order_by(Role.created_date.asc()).paginate(page=page, per_page=per_page)
    return render_template('role.html',department_list=departments, role_records=role_records)

@app.route('/add_or_edit_role', methods=['POST'])
def add_or_edit_role():
    role_id = request.form.get('role_id')
    department_id = request.form.get('department_id')
    role_name = request.form.get('role_name')

    if role_id:  # Edit mode
        role = Role.query.get(role_id)
        if role:
            role.department_id=department_id
            role.role_name = role_name
            db.session.commit()
            flash('Role updated successfully!', 'success')
        else:
            flash('Role not found.', 'error')
    else:  # Add mode
        new_role = Role(
            department_id=department_id,
            role_name=role_name)
        db.session.add(new_role)
        db.session.commit()
        flash('role added successfully!', 'success')

    return redirect(url_for('role'))

@app.route('/delete_role/<int:role_id>', methods=['POST'])
def delete_role(role_id):
    try:
        # Find the statutory record by ID
        role_record = Role.query.get(role_id)
        
        if role_record:
            # Delete all related compliance records
            # Compliance.query.filter_by(statutory_id=statutory_id).delete()
            # Delete the statutory record
            db.session.delete(role_record)
            db.session.commit()
            flash('role and related compliances deleted successfully!', 'success')
        else:
            flash('role record not found.', 'error')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting role: {str(e)}', 'error')
    
    return redirect(url_for('role'))








@app.route('/user',methods=['GET', 'POST'])
def user():
    departments = Department.query.all()
    return render_template('add_user_details.html',departments=departments)

