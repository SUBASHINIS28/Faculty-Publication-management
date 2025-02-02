from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define staff details
staff_data = [
    {
        'Name': 'Sheeba Joice C',
        'Publications': 14,
        'Citations': 285,
        'H-index': 6,
        'Expertise': 'Embedded Systems'
    },
    { 
        'Name': 'Ram Govind',
        'Publications': 40,
        'Citations': 1000,
        'H-index': 20,
        'Expertise': 'Data Science'
    }
]

# Define weights for the impact score
PUBLICATIONS_WEIGHT = 0.1
CITATIONS_WEIGHT = 0.5
H_INDEX_WEIGHT = 0.3

# Function to calculate research impact score
def calculate_impact_score(publications, citations, h_index):
    return (PUBLICATIONS_WEIGHT * publications +
            CITATIONS_WEIGHT * citations +
            H_INDEX_WEIGHT * h_index)

def generate_suggestions(expertise):
    suggestions = {
        'Artificial Intelligence': [
            'Explore ethical implications in AI development.',
            'Participate in AI research conferences and workshops.',
            'Collaborate with interdisciplinary teams on AI applications.'
        ],
        'Machine Learning': [
            'Consider publishing in top ML conferences like NeurIPS.',
            'Focus on deep learning advancements and applications.',
            'Engage in projects that leverage ML for social good.'
        ],
        'Data Science': [
            'Look into data visualization techniques for better insights.',
            'Engage with the latest big data technologies like Hadoop and Spark.',
            'Network with industry leaders at data science summits.'
        ],
        'Blockchain Technology': [
            'Research the impact of blockchain on supply chain management.',
            'Explore decentralized applications (dApps) and their use cases.',
            'Participate in hackathons focusing on blockchain solutions.'
        ],
        'Cybersecurity': [
            'Stay updated on the latest security protocols and vulnerabilities.',
            'Contribute to open-source cybersecurity projects.',
            'Network at cybersecurity conferences and workshops.'
        ],
        'Internet of Things': [
            'Investigate the integration of IoT in smart cities.',
            'Explore edge computing solutions for IoT devices.',
            'Participate in IoT-focused hackathons and challenges.'
        ],
        'Cloud Computing': [
            'Research cloud migration strategies for businesses.',
            'Explore multi-cloud management and optimization techniques.',
            'Engage with the latest cloud security best practices.'
        ],
        'Augmented Reality': [
            'Explore AR/VR applications in education and training.',
            'Participate in immersive technology development workshops.',
            'Collaborate on projects focusing on user experience in AR/VR.'
        ],
        'Natural Language Processing': [
            'Stay updated on advancements in sentiment analysis.',
            'Investigate applications of NLP in chatbots and virtual assistants.',
            'Engage in research on ethical AI in language processing.'
        ],
        'Robotics and Autonomous Systems': [
            'Explore advancements in robotic process automation (RPA).',
            'Investigate applications of drones in various industries.',
            'Participate in robotics competitions and challenges.'
        ],
        'Embedded Systems': [
            'Research the integration of AI in embedded systems.',
            'Explore low-power design techniques for IoT devices.',
            'Collaborate on projects that involve real-time operating systems (RTOS).'
        ],
        'Signal Processing': [
            'Investigate applications of signal processing in communications.',
            'Research new algorithms for audio and image processing.',
            'Engage with industry leaders in signal processing conferences.'
        ],
        'Wireless Communication': [
            'Stay updated on advancements in 5G and beyond technologies.',
            'Research applications of wireless networks in healthcare.',
            'Engage in projects focusing on network optimization.'
        ],
        'Power Electronics': [
            'Explore advancements in renewable energy conversion technologies.',
            'Research power management systems for electric vehicles.',
            'Participate in industry forums focusing on power electronics innovations.'
        ],
        'Control Systems': [
            'Investigate applications of control systems in automation.',
            'Research new control algorithms for complex systems.',
            'Engage with industry experts in control engineering conferences.'
        ],
        'Renewable Energy Systems': [
            'Research the impact of renewable energy on grid stability.',
            'Explore innovations in solar and wind energy technologies.',
            'Participate in renewable energy workshops and seminars.'
        ],
        'VLSI Design': [
            'Stay updated on advancements in semiconductor technology.',
            'Engage in research on design automation tools for VLSI.',
            'Collaborate on projects focusing on energy-efficient circuit design.'
        ],
        'Computer Networks': [
            'Investigate new protocols for secure data transmission.',
            'Research applications of SDN (Software Defined Networking).',
            'Engage with industry leaders at networking conferences.'
        ],
        'Quantum Computing': [
            'Explore the potential applications of quantum algorithms.',
            'Stay updated on developments in quantum hardware.',
            'Participate in workshops focused on quantum information science.'
        ],
        'Photonics and Optical Communication': [
            'Research advancements in fiber-optic technologies.',
            'Explore applications of photonics in medical devices.',
            'Engage with experts in the field at photonics conferences.'
        ]
    }
    return suggestions.get(expertise, ['Explore more research opportunities in your field.'])

# Adding suggestions and impact scores to staff data
for staff in staff_data:
    staff['Suggestions'] = generate_suggestions(staff['Expertise'])
    staff['Impact Score'] = calculate_impact_score(staff['Publications'], staff['Citations'], staff['H-index'])

@app.route('/')
def index():
    # Sort staff_data by impact score
    sorted_staff_data = sorted(staff_data, key=lambda x: x['Impact Score'], reverse=True)
    return render_template('index.html', staff_data=sorted_staff_data)

@app.route('/add_staff', methods=['POST'])
def add_staff():
    name = request.form['name']
    publications = int(request.form['publications'])
    citations = int(request.form['citations'])
    h_index = int(request.form['h_index'])
    expertise = request.form['expertise']

    # Create a new staff entry
    new_staff = {
        'Name': name,
        'Publications': publications,
        'Citations': citations,
        'H-index': h_index,
        'Expertise': expertise,
        'Suggestions': generate_suggestions(expertise),
        'Impact Score': calculate_impact_score(publications, citations, h_index)  # Add impact score
    }

    # Add to staff data
    staff_data.append(new_staff)

    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    # Calculate metrics
    total_publications = sum(staff['Publications'] for staff in staff_data)
    total_citations = sum(staff['Citations'] for staff in staff_data)
    total_h_index = sum(staff['H-index'] for staff in staff_data)

    return render_template('dashboard.html', 
                           total_publications=total_publications, 
                           total_citations=total_citations, 
                           total_h_index=total_h_index,
                           staff_data=staff_data)

if __name__ == '__main__':
    app.run(debug=True)
