from os import path
from pathlib import Path
import sys

import flask
from flask import Flask, render_template
from flask_frozen import Freezer

template_folder = path.abspath('./wiki')

app = Flask(__name__, template_folder=template_folder)
# app.config['FREEZER_BASE_URL'] = environ.get('CI_PAGES_URL')
app.config['FREEZER_DESTINATION'] = 'public'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)


@app.cli.command()
def freeze():
    freezer.freeze()


@app.cli.command()
def serve():
    freezer.run()


@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/favicon.ico')
def favicon():
    return render_template(path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/<page>')
def pages(page):
    if page in ['authors']:
        students = [
            {"name": "John Doe", "grade": "Grade 10", "title": "My Journey",
                "description": "A short description of my journey.", "page": "Page 1"},
            {"name": "Emily Smith", "grade": "Grade 11", "title": "Exploring New Horizons",
                "description": "Passionate about astronomy and mathematics."},
            {"name": "James Johnson", "grade": "Grade 12", "title": "Beyond the Classroom",
                "description": "Active in community service and sports."},
            {"name": "Sophia Williams", "grade": "Grade 10", "title": "Artistic Expressions",
                "description": "Loves painting and creative writing."},
            {"name": "Michael Brown", "grade": "Grade 11", "title": "Tech Enthusiast",
                "description": "Interested in coding and robotics."},
            {"name": "Isabella Jones", "grade": "Grade 12", "title": "Global Citizen",
                "description": "Passionate about environmental sustainability."},
            {"name": "William Davis", "grade": "Grade 10", "title": "Sports and Fitness",
                "description": "Competitive swimmer and fitness enthusiast."},
            {"name": "Olivia Miller", "grade": "Grade 11", "title": "Science Innovator",
                "description": "Researching biochemistry and genetics."},
            {"name": "Daniel Wilson", "grade": "Grade 12", "title": "Future Entrepreneur",
                "description": "Founder of a student-run business."},
            {"name": "Emma Garcia", "grade": "Grade 10", "title": "Literary Enthusiast",
                "description": "Writes poetry and short stories."},
            {"name": "Alexander Martinez", "grade": "Grade 11", "title": "Musician's Journey",
                "description": "Plays violin and composes music."},
            {"name": "Ava Hernandez", "grade": "Grade 12", "title": "Community Leader",
                "description": "Organizes charity events and volunteers."},
            {"name": "Noah Lopez", "grade": "Grade 10", "title": "Future Engineer",
                "description": "Builds robots and participates in STEM competitions."},
            {"name": "Mia Gonzalez", "grade": "Grade 11", "title": "Dance and Expression",
                "description": "Dancer and choreographer."},
            {"name": "Elijah Perez", "grade": "Grade 12", "title": "Political Activist",
                "description": "Advocates for youth rights and education reform."},
            {"name": "Charlotte Taylor", "grade": "Grade 10", "title": "Nature Enthusiast",
                "description": "Hiker and wildlife photographer."},
            {"name": "Lucas Moore", "grade": "Grade 11", "title": "Future Scientist",
                "description": "Researching physics and astronomy."},
            {"name": "Grace Lee", "grade": "Grade 12", "title": "Cultural Ambassador",
                "description": "Promotes cultural exchange and understanding."},
            {"name": "Benjamin Scott", "grade": "Grade 10", "title": "Theatre Arts",
                "description": "Acting and directing in school productions."},
            {"name": "Chloe Clark", "grade": "Grade 11", "title": "Health and Wellness",
                "description": "Yoga instructor and nutrition advocate."},
            {"name": "Jacob Turner", "grade": "Grade 12", "title": "Future Architect",
                "description": "Designs buildings and urban spaces."},
            {"name": "Lily Baker", "grade": "Grade 10", "title": "Animal Rights Advocate",
                "description": "Volunteers at animal shelters and rescues."},
            {"name": "Ryan Rodriguez", "grade": "Grade 11", "title": "Mathematics Prodigy",
                "description": "Competes in math Olympiads."},
            {"name": "Samantha Hall", "grade": "Grade 12", "title": "Future Physician",
                "description": "Interns at a local hospital and studies medicine."},
            {"name": "Luke Young", "grade": "Grade 10", "title": "Technology Innovator",
                "description": "Develops apps and software."},
            {"name": "Natalie King", "grade": "Grade 11", "title": "Environmental Advocate",
                "description": "Organizes clean-up campaigns and recycling initiatives."},
            {"name": "Gabriel Scott", "grade": "Grade 12", "title": "Future Filmmaker",
                "description": "Directs short films and documentaries."},
            {"name": "Zoe Walker", "grade": "Grade 10", "title": "Creative Writer",
                "description": "Writes fiction novels and poetry."},
            {"name": "Joshua Green", "grade": "Grade 11", "title": "Social Justice Warrior",
                "description": "Raises awareness about human rights issues."},
            {"name": "Madison Hill", "grade": "Grade 12", "title": "Future Lawyer",
                "description": "Debates and participates in mock trials."},
            {"name": "Aiden Carter", "grade": "Grade 10", "title": "Sports Star",
                "description": "Plays soccer and basketball competitively."},
            {"name": "Sophie Mitchell", "grade": "Grade 11", "title": "Future Journalist",
                "description": "Writes for the school newspaper and reports on local events."},
            {"name": "Jackson Young", "grade": "Grade 12", "title": "Artistic Visionary",
                "description": "Paints and exhibits artwork."},
            {"name": "Avery Turner", "grade": "Grade 10", "title": "Future Astronomer",
                "description": "Stargazer and telescope enthusiast."},
            {"name": "Hailey Adams", "grade": "Grade 11", "title": "Tech Wizard",
                "description": "Develops AI applications and software."},
            {"name": "Caleb Roberts", "grade": "Grade 12", "title": "Music Producer",
                "description": "Creates electronic music and produces tracks."},
            {"name": "Ella Nelson", "grade": "Grade 10", "title": "Community Volunteer",
                "description": "Organizes food drives and volunteers at shelters."},
            {"name": "Julian Hughes", "grade": "Grade 11", "title": "Future Economist",
                "description": "Studies global economics and finance."},
            {"name": "Makayla Parker", "grade": "Grade 12", "title": "Theatre Performer",
                "description": "Acting and singing in musical theatre productions."},
            {"name": "Connor Gray", "grade": "Grade 10", "title": "Future Biologist",
                "description": "Researches marine biology and conservation."},
            {"name": "Abigail Collins", "grade": "Grade 11", "title": "Animal Rights Advocate",
                "description": "Works to protect endangered species."},
            {"name": "Owen Murphy", "grade": "Grade 12", "title": "Future Engineer",
                "description": "Designs and builds model airplanes."},
        ]

        return render_template(str(Path('pages')) + '/' + page.lower() + '.html', students=students)
    return render_template(str(Path('pages')) + '/' + page.lower() + '.html')


# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freeze()
    else:
        app.run(port=8080)
