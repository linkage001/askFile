class Question:
    question: str
    options: list[str]

    def __init__(self, question, options):
        self.question = question
        self.options = options


question = """education
Choose the option that best describes the candidate's situation:

<<a>> Complete elementary education

<<b>> Complete secondary education

<<c>> Complete technical education

<<d>> Complete higher education

<<e>> Complete postgraduate education"""

options = {
    'a': 'Complete elementary education',
    'b': 'Complete secondary education',
    'c': 'Complete technical education',
    'd': 'Complete higher education',
    'e': 'Complete postgraduate education'
}

question1 = """exp_retail
Please choose the option that best describes your level of experience working with large retail networks such as Kibabo/Kero/Amgomart/Shoprite/Descontão/Alimenta Angola:

<<a>> Less than one year

<<b>> Between 1-3 years

<<c>> Between 3-5 years

<<d>> Between 5-7 years

<<e>> More than 7 years"""

options1 = {
    'a': 'Less than one year',
    'b': 'Between 1-3 years',
    'c': 'Between 3-5 years',
    'd': 'Between 5-7 years',
    'e': 'More than 7 years'
}

question2 = """exp_tech
What is your level of experience in office products retail companies, similar to NCR?:

<<a>> Less than 1 year

<<b>> Between 2-5 years

<<c>> Between 5-10 years

<<d>> I have never worked for such a company before

<<e>> Over 10 years"""

options2 = {
    'a': 'Less than 1 year',
    'b': 'Between 2-5 years',
    'c': 'Between 5-10 years',
    'd': "I have never worked for such a company before",
    'e': 'Over 10 years'
}

question3 = """communication
Please choose the option that best describes your communication skills:

<<a>> Excellent - I am an effective and clear communicator, able to adjust my style to suit different audiences.

<<b>> Very good - I have strong communication skills and can express myself well in writing and speaking.

<<c>> Good - I am capable of communicating effectively, but may need some practice in certain situations.

<<d>> Fair - I can get my point across, but could benefit from improving my communication skills.

<<e>> Poor - I struggle to communicate effectively and often have difficulty expressing myself."""

options3 = {
    'a': 'Excellent - I am an effective and clear communicator, able to adjust my style to suit different audiences.',
    'b': 'Very good - I have strong communication skills and can express myself well in writing and speaking.',
    'c': "Good - I am capable of communicating effectively, but may need some practice in certain situations.",
    'd': "Fair - I can get my point across, but could benefit from improving my communication skills.",
    'e': "Poor - I struggle to communicate effectively and often have difficulty expressing myself."
}

question4 = """degree
What is your highest level of education?

<<a>> Currently enrolled in a bachelor's degree program

<<b>> Bachelor's degree already completed

<<c>> Some college coursework, but no degree earned

<<d>> High school diploma only

<<e>> Less than high school diploma."""

options4 = {
    'a': 'Currently enrolled in a bachelor\'s degree program',
    'b': 'Bachelor\'s degree already completed',
    'c': 'Some college coursework, but no degree earned',
    'd': 'High school diploma only',
    'e': 'Less than high school diploma'
}

question5 = """exp_manegement
Please choose the option that best describes your most relevant management experience to act as Sales Manager or Sales Executive Assistant:

<<a>> Leading technical support teams for over 5 years

<<b>> Managing physical store with team of 10 people for 3 years

<<c>> Working as an individual sales representative for 2 years without management experience

<<d>> Leading remote sales team in a technology startup for 4 years

<<e>> No previous managerial experience"""

options5 = {

    'a': 'Leading technical support teams for over 5 years',

    'b': 'Managing physical store with team of 10 people for 3 years',

    'c': 'Working as an individual sales representative for 2 years without management experience',

    'd': 'Leading remote sales team in a technology startup for 4 years',

    'e': 'No previous managerial experience'

}

question6 = """exp_sales
To what extent are you comfortable developing and implementing efficient sales strategies?

<<a>> With great ease, I already have proven experience in this regard

<<b>> I can do that with some additional training

<<c>> I have basic knowledge about sales strategies but need to improve my skills

<<d>> I prefer to follow detailed instructions rather than creating my own strategies

<<e>> I have never been involved in the creation of sales plans"""

options6 = {

    'a': 'With great ease, I already have proven experience in this regard',

    'b': "I can do that with some additional training",

    'c': "I have basic knowledge about sales strategies but need to improve my skills",

    'd': "I prefer to follow detailed instructions rather than creating my own strategies",

    'e': "I have never been involved in the creation of sales plans"

}

question7 = """exp_clients
Please choose the option that best describes your ability to maintain solid relationships with clients and key partners:

<<a>> Excellent, I possess strong interpersonal skills and communication

<<b>> Good, I usually have good relations with my professional contacts

<<c>> Average, sometimes I face difficulties establishing lasting bonds

<<d>> Weak, I prefer focusing on transactions themselves rather than relationships

<<e>> No practical experience maintaining relationships with clients or partners"""

options7 = {

    'a': 'Excellent, I possess strong interpersonal skills and communication',

    'b': 'Good, I usually have good relations with my professional contacts',

    'c': 'Average, sometimes I face difficulties establishing lasting bonds',

    'd': 'Weak, I prefer focusing on transactions themselves rather than relationships',

    'e': 'No practical experience maintaining relationships with clients or partners'

}

questions = [
    Question(question, options),
    Question(question1, options1),
    Question(question2, options2),
    Question(question3, options3),
    # Question(question4, options4),
    Question(question5, options5),
    Question(question6, options6),
    Question(question7, options7),
]
