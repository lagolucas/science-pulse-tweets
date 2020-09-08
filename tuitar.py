if __name__ == '__main__':
    from database import TweetBotParams
    from database import TweetBotQueue
    import twitter

    languages = ['pt']
    
    for language in languages:
        first_tweet = TweetBotParams.select().where((TweetBotParams.slug == 'start') & (TweetBotParams.lang == language)).get()
        previous_status = twitter.start_thread(first_tweet)
        
        
        status_list = TweetBotQueue.select(TweetBotQueue, TweetBotParams).join(TweetBotParams).where((TweetBotQueue.param.lang == language) & (TweetBotQueue.bot_flag == False))

        for status in status_list:
            previous_status = twitter.tweet(status, previous_status)
            status.bot_flag = True
            status.save()

        last_tweet = TweetBotParams.select().where((TweetBotParams.slug == 'end') & (TweetBotParams.lang == language)).get()
        twitter.end_thread(last_tweet, previous_status)