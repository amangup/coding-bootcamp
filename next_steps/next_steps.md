# How to become a professional programmer?

In this document, we will discuss what you can do to take your learning further and become a programmer professionally, or enhance your career if you're already one.

There are a few questions that one would have, and few choices for one to make. In this document I will try to help you find answers.

1. What do professional programmers do?
2. What kind of programming jobs exist?
3. What do employers want from candidates?
4. How can you keep learning to improve your programming skills?
5. How to prepare for interviews?

I will try to answer this questions with the context of what we've learned in this bootcamp, and what I believe are the current trends in the tech industry.

## What do professional programmers do?

Programmers spend their days writing code. I spend more than 70% of my time in my IDE (IntelliJ or PyCharm) or in the terminal. 

A fundamental skill, in addition to being able to write code, is to be able to understand requirements well. The goal of writing programs is to build applications for users. This is a highly valued skill - in most companies, a senior programmer is expected to have the ability to talk to the product and business teams, understand their needs, and then be able to come up with a plan to implement the software which meets those needs.
  
### Programming is a team activity

- For any full application development, two or more programmers are usually required and they may have expertise in different areas of programming. Thus, programming is inherently a team activity.
- Most teams also have a some people who have more experience and others people who are relative newcomers. Mentoring new programmers is usually an essential part of the role of experienced team members.
- It's uncommon for any one software engineer to know all the technologies being used for building a certain product. 

My point is that no programming team expects to hire engineers who know how to deliver the product from start to end by themselves. There is little point in building your capabilities to be able to do that. Instead, it's more useful to make yourselves comfortable with working as part of a team, and to learn from the experienced members of your team.

## What kind of programming jobs exist?

Programming is used in numerous scenarios to build products for consumers (B2C), other businesses (B2B) or for internal applications in a company. A programmer's responsibility depends on what the product is, who the consumer is and what expertise the programmer has. 

- How is the software accessed by an user? Is it a mobile app, a website, or a desktop application?
  - e.g. If the interface is a mobile app, Android and iOS are the two most popular mobile OSes. They have their own proprietary development _environment_ to build applications for them. The company would need programmers who know how have experience working in that environment.
  - e.g If the interface is a web app, then we already know that we need combination of an HTTP server (like we built using Python Flask), Javascript and CSS to build a good web app. There are programmers/designers specializing individually in these technologies, or those who can build in all three technologies (also known as _full stack programmers_).
  
- What kind of logic does the product need?
  - e.g. If the application stores massive amount of user's data (like Dropbox), then they need programmers who understand the principles of data storage, compression, caching of data, etc.
  - e.g. If the application serves videos (like Vimeo), then they need programmers who are experts at video streaming technology.
  - e.g. If the application requires data mining (like Google Search), then they need programmers who have good background in statistics, data science, and data mining techniques.
  
Programming jobs can be categorized into the following broad categories:

- **Client side** programming - like building mobile app, writing Javascript for web app etc.
- **Frontend** programming - writing the logic of the web server which communicates with the client.
- **Backend** programming - working on the data systems needed for the application.
  - This can be further broken into two parts: Engineers who understand computer systems well and are responsible to write and maintain high performance data services, and engineers who are good at data science.
  
Let's discuss each in a little more detail.  
  
### Client side programming

- To be a client side programmer, typically Javascript is considered an essential requirement (even if one is not building a web app for a given project).
   - There are libraries like **React** and **Angular** which help you implement sophisticated functionality using smaller, simpler code.
   - There are libraries like **ReactNative** that allows one to write Android and iOS apps using Javascript. 
- For iOS and Android developers, programmers need to understand the Swift and/or Objective-C language (for iOS) and Java (for Android).
   - In addition to knowing the language, one needs to have experience building apps for these platforms. These platforms have unique features and constraints (like using device's GPS location) which you need to learn to use.

There is a way for Python programmers to write client code for web applications using [**Webassembly**](https://webassembly.org/getting-started/developers-guide/). It's not widely used at the moment, but it's slowly gaining momentum, especially among programmers don't know or like Javascript.

### Frontend programming

- Pretty much any technology product has a server which the client needs to interact with (not just computers or phones, but even your smart microwave contacts a web server).
- Python is becoming the most popular language to write web servers in (mainly using Django or Flask). Languages like Java, C++, Go and Ruby are also widely used for these purposes.
- You also need to understand how to make web servers use data systems like SQL Databases (which we learnt in this course), _NoSQL_ Databases (like [MongoDB](https://www.mongodb.com) or [BigTable](https://cloud.google.com/bigtable/), and high performance caching databases (like [Redis](https://redis.io/) and [Memcached](https://memcached.org/)).

### Backend programming

- For the high performance data servers, typically languages like C, C++ or Go are used to write those servers.
  - In addition to knowing languages, working on these systems needs a deep knowledge of how computer systems work (computer architecture, operating system, networks) etc.
  - One aspect of the data systems is building _big data pipelines_. This is a system which can collect and do data transformations on huge amounts of data reliably using a cluster of computers. Commonly used platforms include **Hadoop** (need to know Java) and **Spark** (need to know Scala, Java or Python).
  
- For data science and analysis, Python is now the most popular language for newcomers entering this field. This is because of multiple reasons, one of them being that there is wide array of libraries which help you design advanced analysis or machine learning solutions with very simple APIs.  
  - Some famous libraries: **Numpy** (for efficient data containers), **Scipy** (for numerical computation), **Scikit-learn** (for machine learning), **pandas** (for data transformations), **TensorFlow** and **Keras** (for deep learning). This is a small sample; there are tens or hundreds more libraries which are also very useful and popular.
  
### Common skills

There are some common skills that any developer needs to have:

- Know how to use **Git**. This is a system for maintaining history of code and work collaboratively in a team.

    https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control  
    https://guides.github.com/activities/hello-world/

- Know how to use the terminal. Terminal helps you do things like copying, moving, deleting files, looking inside them and much much more. There is a bit of learning curve, but once you get comfortable it is always quicker to use the terminal than using GUI.

    https://ryanstutorials.net/linuxtutorial/  
    https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line  
    
## What do employers look for?

Any employer needs to determine if the candidate has skills and experience in writing programs and building software technology similar to what they need them to build at their job. How do they verify this?

- Do you have a computer science degree (BS, MS, PhD) from a reputed school?
- Have you worked as a programmer at a company previously, and if yes, what kind of work did you do there?

For this audience, I assume that the answer to this question could be no. How else can you shine in front of an employer?

1. Build a portfolio of projects you executed on your own, or with some friends. 
   - This is my top recommendation for anyone trying to get a programming job or changing the programming field they want to work on.
   - This is incredibly valuable for the employer. Not only they can see what you've built and how complex your project is, they can also read your code (something they cannot do for the code you wrote at your previous company).
   

2. Participate in programming competitions and "Hackathons" (programming competitions where participants convert an idea into a working prototype in a limited amount of time).
   - In the bay area, and worldwide, there are a number of Hackathons that are organized. Here is an example of the search results for [Hackathon on EventBrite](https://www.eventbrite.com/d/ca--san-francisco/hackathon/):
   - There are many websites which regularly organize coding challenges. Programmers can build their score and credibility by participating and performing well in them repeatedly over time. Here is a [list of such websites](https://medium.freecodecamp.org/the-10-most-popular-coding-challenge-websites-of-2016-fb8a5672d22f):
   - Both of these help you get noticed by an employer. 
  
3. Start your own company :-)
   - Instead of waiting someone else to employ you, you can employ yourself.
   - I don't have personal experience, but from what I've learnt from friends who've tried this path: one learns a lot when they are the ones responsible for putting the actual product in the hand of consumers. You have to learn to work and deliver under pressure (limited time, limited money, etc.).
   - Even if you don't eventually succeed, I know that such experience is highly valued if you had genuinely new ideas and tried to build a great product.
 
### Where to find job listings
There are numerous websites (major ones like LinkedIn and Glassdoor), but I wanted to highlight:
   - [AngelList](https://angel.co/) - this is used by startups and smaller companies. When you are trying to switch to a programming career, there is a greater chance that a smaller firm will hire you, as opposed to companies like Google, Microsoft, Facebook, etc.
   - [Upwork](https://www.upwork.com/) - This is for freelance jobs. Once you're confident about your skills, you can search for contract jobs that other's have put here and pick those up. I know friends who've used this platform to gain additional income.
  
## How to keep learning?

For programming jobs, it is essential that you keep learning new things. Technologies change rapidly, and there are so many technologies already out there that for any new project, you would usually need to learn a new one.

- Get comfortable with learning new things on your own. 
   - This is extremely important - there is usually so much to learn that you can't expect all your learning to happen in a classroom somewhere.
   - Use books or online courses as learning material.
   - Practice everything you learn. Majority of the learning happens as you attempt to build something by trial and error.
   - Use forums (online or where you live) to ask questions. The SF Bay Area also has numerous meetups meant for this purpose.
   
- Always work on a personal project
  - When you work on a project, you will usually not be able to complete it without learning something new. This makes learning a mandatory activity instead of an optional one.
  - Show your project to others! This is useful to get motivation, and also get feedback from other people who can think like prospective users.
  
- Join advanced coding bootcamps.
  - Now that you are comfortable with coding, you can join more classes to take your skills further.
  - Another benefit of going through such a bootcamp is that many of these put you in front of prospective employers.  
  
## Interviews

A hiring process usually goes like this:
1. You share your resume and portfolio.
2. If the employer likes it, they talk to you, and sometimes give you a programming challenge to complete from home.
3. Based on that initial evaluation, the employer would typically bring you in for on-site interviews.

The interviews typically focus on these aspects:

1. Talking about your background. From experience of having taken many such interviews, I know the goal of this discussion is to determine if you actually were hands on and deeply involved in a project. You need to have had a major contribution to that project to pass this phase. And the project must have forced _you_ to solve some non-trivial problem.

2. Give you challenges. These can be:
   - Solve an algorithm problem - The interviewer gives you a problem statement (like finding the shortest path in a city), and you are expected to come with a precise step by step solution (but not necessarily write code) to that problem.
   - Ask mathematical or logical puzzles ([like these](http://www.crazyforcode.com/top-10-interview-puzzles/)) - programming interviews can contain puzzles which are used to test your [problem solving skills](https://www.job-interview-site.com/problem-solving-skills-examples-of-problem-solving-skills.html).
   - Ask you to write code. This is similar to the algorithm problem, but usually the problem is simpler from the logic POV. You are expected to write the exact code that will solve the problem - either in a language they specify or any language that you are comfortable with. You are judged by your ability to write concise readable code that takes care of all input cases, and uses an optimal algorithm. Many of the assignments in this course are examples of such problems.
  
3. Open ended discussions. These are typically real life problems which don't necessarily have a right answer. You are judged on how you are able to take constraints into account and come up with a potential solution which balances the many trade offs that are usually involved.

### How to prepare for interviews

Most of the interview preparation is essentially solving many problems, like the ones you expect them to ask, before the interview. There are hundreds of sites which has sample interview questions. This [quora answer](https://www.quora.com/What-are-the-top-20-websites-for-interview-preparation) has many such sites listed in the answers.

It's a good idea to practice mock interviews either with friends who are professional programmers. Nowadays, there are even startups that focus on practicing for interviews (like [Interviewing.io](https://interviewing.io/faq/)). 

## Be patient and don't stop learning
In the first lecture of this course, I shared this post from a Google Director of Research

[Teach Yourself Programming in Ten Years](http://norvig.com/21-days.html)

I want you to read this yourself, so I won't spoil it here. But in a nutshell, it says that like any skill, programming is not something which you can become an expert at in a week, or even 6 months. It's a lifelong task and you must be patient and devoted.
