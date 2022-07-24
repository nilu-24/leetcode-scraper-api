
import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify,request
app = Flask(__name__)


def findQuestion(problem_name):

    #https://stackoverflow.com/questions/56608480/parsing-leetcode-question-content-with-requests-and-beautifulsoup

    #scraping data using bs4
    
    data = {"operationName":"questionData","variables":{"titleSlug":problem_name},"query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}
    r = requests.post('https://leetcode.com/graphql', json = data).json()

    try:
        questionHTML = bs(r['data']['question']['content'], "html.parser")
        title = r['data']['question']['title']
        questionId = r['data']['question']['questionId']
        difficulty = r['data']['question']['difficulty']

        return jsonify({"questionId": questionId,
        "title":title,
        "question":str(questionHTML),
        "difficulty":difficulty})

    except:
        return "Question Not Found"

@app.route('/',methods=['GET'])
def find():
    questionName = str(request.args['question'])
    return findQuestion(questionName)


