__author__ = 'enstulen'

videoer = ["http://www.youtube.com/watch?v=-840keiiFDE&t=1m40s", "http://www.youtube.com/watch?v=GpNSip5gyKo", "http://www.youtube.com/watch?v=sXX5drqRD9s", "http://www.youtube.com/watch?v=ZFngtBIxRPk", "http://www.youtube.com/watch?v=OZBWfyYtYQY", "http://www.youtube.com/watch?v=7LKHpM1UeDA"]

for n in range(len(videoer)):
    print(videoer[n].replace(videoer[n][0:31], "youtu.be/"))
