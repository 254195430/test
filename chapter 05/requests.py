from flask import Flask, render_template, request, jsonify, redirect, session
from flask import abort
from flask_cors import CORS, cross_origin
from flask import make_response, url_for
import json
import random
from pymongo import MongoClient
from time import gmtime, strftime

# connection to MongoDB Database
connection = MongoClient("mongodb://localhost:27017/")

class Requests:
    # List users
    def list_users():
        api_list=[]
        db = connection.cloud_native.users
        for row in db.find():
            api_list.append(str(row))
        # print (api_list)
        return jsonify({'user_list': api_list})

    # List specific users
    def list_user(user_id):
        print (user_id)
        api_list=[]
        db = connection.cloud_native.users
        for i in db.find({'id':user_id}):
            api_list.append(str(i))

        if api_list == []:
            abort(404)
        return jsonify({'user_details':api_list})

    # List specific tweet
    def list_tweet(user_id):
        print (user_id)
        db = connection.cloud_native.tweets
        api_list=[]
        tweet = db.find({'id':user_id})
        for i in tweet:
            api_list.append(str(i))
        if api_list == []:
            abort(404)
        return jsonify({'tweet': api_list})

    # Adding user
    def add_user(new_user):
        api_list=[]
        print (new_user)
        db = connection.cloud_native.users
        user = db.find({'$or':[{"username":new_user['username']} ,{"email":new_user['email']}]})
        for i in user:
            print (str(i))
            api_list.append(str(i))

        # print (api_list)
        if api_list == []:
        #    print(new_user)
           db.insert(new_user)
           return "Success"
        else :
           abort(409)

    # Deleting User
    def del_user(del_user):
        db = connection.cloud_native.users
        api_list=[]
        for i in db.find({'username':del_user}):
            api_list.append(str(i))

        if api_list == []:
            abort(404)
        else:
           db.remove({"username":del_user})
           return "Success"

    # List tweets
    def list_tweets():

        api_list=[]
        db = connection.cloud_native.tweets
        for row in db.find():
            api_list.append(str(row))
        # print (api_list)
        return jsonify({'tweets_list': api_list})


    # Adding tweets
    def add_tweet(new_tweet):
        api_list=[]
        print (new_tweet)
        db_user = connection.cloud_native.users
        db_tweet = connection.cloud_native.tweets

        user = db_user.find({"username":new_tweet['tweetedby']})
        for i in user:
            api_list.append(str(i))
        if api_list == []:
           abort(404)
        else:
            db_tweet.insert(new_tweet)
            return "Success"

    def upd_user(user):
        api_list=[]
        print (user)
        db_user = connection.cloud_native.users
        users = db_user.find_one({"id":user['id']})
        for i in users:
            api_list.append(str(i))
        if api_list == []:
           abort(409)
        else:
            db_user.update({'id':user['id']},{'$set': user}, upsert=False )
            return "Success"