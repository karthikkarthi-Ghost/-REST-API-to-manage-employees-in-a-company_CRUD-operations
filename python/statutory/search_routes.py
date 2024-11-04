from flask import render_template, request, redirect, url_for, flash
from python.config import app  # Updated import
from python.models import Statutory,Role,Department# Updated import

@app.route('/search')
def search():
    query = request.args.get('q')
    template = request.args.get('template')
    results = Statutory.query.filter(Statutory.statutory_name.ilike(f'%{query}%')).all()
    
    if template == 'statutoryform':
        return render_template('statutoryform.html', records=results)
    elif template == 'complianceform':
        return render_template('complianceform.html', records=results)
    else:
        flash("Invalid template specified.", "error")
        return redirect(url_for('index'))

@app.route('/searchrole')
def searchrole():
    query = request.args.get('q')
    template = request.args.get('template')
    results = Role.query.filter(Role.statutory_name.ilike(f'%{query}%')).all()
    
    if template == 'roleform':
        return render_template('role.html', records=results)
    
    else:
        flash("Invalid template specified.", "error")
        return redirect(url_for('role'))
    
@app.route('/searchdepartment')
def searchdepartment():
    query = request.args.get('q')
    template = request.args.get('template')
    results = Department.query.filter(Department.statutory_name.ilike(f'%{query}%')).all()
    
    if template == 'roleform':
        return render_template('department.html', records=results)
    
    else:
        flash("Invalid template specified.", "error")
        return redirect(url_for('department'))