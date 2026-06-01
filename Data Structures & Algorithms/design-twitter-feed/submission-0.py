class Twitter:

    def __init__(self):
        self.f = defaultdict(bool)
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for i in range(len(self.tweets) - 1, -1, -1):
            u, t = self.tweets[i]
            if (userId, u) in self.f and self.f[userId, u] or u == userId:
                res.append(t)
            if len(res) == 10:
                break
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId, followeeId] = True

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.f[followerId, followeeId] = False
