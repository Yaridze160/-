from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Job
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def addUser(surname, name, age, position, speciality, address, email, password):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    user.set_password(password)
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def addJob(leader, jobname, worksize, coloborators, startdate, enddate, is_finished):
    job = Job()
    job.team_leader = leader
    job.job = jobname
    job.worksize = worksize
    job.collaborators = coloborators
    job.start_date = startdate
    job.end_date = enddate
    job.is_finished = is_finished
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


@app.route("/", methods=['GET'])
def joblist():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job).all()
    users = db_sess.query(User).all()
    names = []
    for user in users:
        names.append([user.surname, user.name])
    return render_template("joblist.html", jobs=jobs, names=names)


def main():
    db_session.global_init("db/mars.db")
    # addUser("Scott", "Ridley", 21, 'captain', 'research engineer', "module_1", "scott_chief@mars.org", "123")
    # addUser("Red", "Mike", 32, 'team member', 'mechanic', "module_1", "RedGuy@mars.org", "123")
    # addUser("Zmirko", "Denis", 25, 'captain assistant', 'doctor', "module_2", "Rud1@mars.org", "123")
    # addUser("Miheev", "Anya", 20, 'team member', 'engineer architect', "module_2", "MihAn@mars.org", "123")
    # addJob(1, "deployment of residential modules 1 and 2", 15, "2, 3", dt.datetime.now(), None, False)
    app.run(port=8080, host='127.0.0.1')

    
if __name__ == '__main__':
    main()
