import requests
from bs4 import BeautifulSoup as bs
from flask import Flask, jsonify

def findQuestion(problem_name):

    data = {"operationName":"questionData","variables":{"titleSlug":problem_name},"query":"query questionData($titleSlug: String!) {\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    boundTopicId\n    title\n    titleSlug\n    content\n    translatedTitle\n    translatedContent\n    isPaidOnly\n    difficulty\n    likes\n    dislikes\n    isLiked\n    similarQuestions\n    contributors {\n      username\n      profileUrl\n      avatarUrl\n      __typename\n    }\n    langToValidPlayground\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    codeSnippets {\n      lang\n      langSlug\n      code\n      __typename\n    }\n    stats\n    hints\n    solution {\n      id\n      canSeeDetail\n      __typename\n    }\n    status\n    sampleTestCase\n    metaData\n    judgerAvailable\n    judgeType\n    mysqlSchemas\n    enableRunCode\n    enableTestMode\n    envInfo\n    libraryUrl\n    __typename\n  }\n}\n"}
    r = requests.post('https://leetcode.com/graphql', json = data).json()

    try:
        soup = bs(r['data']['question']['content'], "html.parser")
        #print(soup)
        title = r['data']['question']['title']
        questionId = r['data']['question']['questionId']
        difficulty = r['data']['question']['difficulty']

        question =  soup.get_text()

        image = soup.find_all("img")

        #print(soup)

        return {"questionId": questionId,
        "title":title,
        "question":soup,
        "difficulty":difficulty}


    except:
        return "Question Not Found"

findQuestion("trapping-rain-water")



