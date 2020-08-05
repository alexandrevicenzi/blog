---
title: Is my project failing?
date: 2020-08-05
slug: is-my-project-failing
description: Failure can come in many forms and shapes, but there are usually signs along the way that may help you fix it before being too late.
summary: In today's article, I'm going to talk about things that I've seen over the years that slowly were contributing to the failure of a project, and how to avoid it.
images:
  - /images/content/failure.jpg
tags:
  - engineering
  - good-practices
  - standards
  - management
  - agile
---

{{< figure src="/images/content/failure.jpg" width="300px" alt="Failure" caption="Photo by [John T](https://unsplash.com/@john_visualz) on [Unsplash](https://unsplash.com/)" >}}

Failure can come in many forms and shapes, I've seen a company work on two major projects for years that never were launched, an interesting project that lost all the good engineers due to bad management, difficult and expensive project maintenance, and tools and technologies from over 20 years ago being used, and more.

Yet, none of these companies filed for bankruptcy. The companies are still there, profitable (I think), which means that sometimes failure is not a total disaster, but it may set you back.

In today's article, I'm going to talk about things that I've seen over the years that slowly were contributing to the failure of a project, and how to avoid it.

## Being fast instead of Agile

Agile is a way to quickly interact, adapt, or change, it also means that you usually have fast deliverables because you work in iterations, delivering small pieces every time, but in the end, the entire project may still take hundreds of hours to be completed.

You should think of it as a development mindset, a way of dealing with requirements, changes, and all bumps that you will find while working on a project, and not as a way to deliver a project in less time.

## Scarce documentation

The lack of documentation introduces many problems, from development to customer support. In engineering there's a thought that documenting things is a waste of time, someone can read the code and understand right? Yes, one can understand what the code is doing, but they won't magically figure out why it is that way, or what was the business idea behind it.

Documenting code, architecture, and all other bits and pieces are good for developers, it will save you time once a problem appears because there's something in place to understand the why's.

No less important, documentation for customers/users is equally or more important. The lack of proper documentation will be a burden for your support team. Proper documentation and a knowledge base are important for users. When users can't solve problems by themselves they open a ticket and that costs money.

## Poor test coverage

TDD, BDD, DDD, unit test, integration test, load/stress test, E2E, the list goes on. Yes, it seems an overload of testing methods and practices, but everything has its place and time. I'm not going to discuss the differences between each, you should know that testing is as important as coding new features.

Testing your product is the easiest and cheapest way to find bugs. It's the easiest because a bug or a bad implementation can be quite costly to fix once it's in production and the bug can also become some sort of feature for some customers/users. It's cheap because a bug can impact your product and this can impact your revenue directly.

There's not too much testing I think, the biggest the coverage the more confident you can be with new releases. Yes, testing it properly takes time, but it also saves time in the future.

## Wrong tooling

Choosing the wrong tools for the job is a problem. C++ for web development works, but is it the right tool? Probably not. There are programming languages and frameworks more suitable for this scenario.

There may be a range of tools for a particular problem, finding something that the team is capable of maintaining is the safest bet. You don't want to choose Perl and figure out later on that it is difficult to find skilled people in this particular language.

Using the latest bleeding-edge framework that someone wrote over one night, posted on Hacker News, and got 10k stars on GitHub on a single day is also something that you want to avoid. Tooling with a great community around can easily come in handy once you need help.

## Wrong size

“Premature optimization is the root of all evil” is a famous saying among software engineers and it's credited to Donald Knuth. Yes, premature optimization can be bad, but you can probably predict the growth of your project and it should be possible to scale it if required, with minimal effort, at least to some extent.

You can build an amazing project, but if the project can't keep up with its user base that's going to be a big problem. I'm pretty sure that you don't want to rewrite something entirely or partially after just 3 months of launch.

Predicting if a project will go viral is impossible, but assuming that you are not building a new social network, you can still have some idea or envision the project for the next 6 months to maybe up to 2 years. If you can, great, make it in a way that the project can accommodate future changes with ease, but you don't need to implement until it's required.

## Not listening to developers

Who understands the project better than the ones that wrote it? Listening to their concerns is important, taking actions once they notify about something that does not seem right is strongly advised.

Developers will come with scale and maintenance concerns, they will ask for time to work on things that won't deliver anything valuable for customers at first glance, but what people don't understand is that there's a hidden cost to keep services up and running. Would you rather deliver a new feature or work on tasks to keep all systems operational? Finding time for maintenance and updates is also important.

## Lack of understanding

Understanding customers and/or stakeholders can be hard, that's why you need to invest time in requirements and also validate it before any work is done.

Building the wrong set of features as you know can be catastrophic, but building the correct requirements that were poorly described and do not fit any use case is as bad as it.

Requirements may not be enough to fully capture someone's idea or vision, thus good communication and fast iterations for prototypes can be crucial to success.

## Rushing too much

Everyone wants to deliver things ASAP these days, but rushing releases to the point that you are delivering a low-quality software is the worst that you can possibly do.

Buggy software will cause customers and users to lose trust and may lead them into competitors and/or alternatives. I would rather release something that has fewer features but works, than a gigantic piece that does not.

## Imbalance

A team must be in harmony most of the time, constant drama and divergences can affect the project quality, readiness, timelines, and even cause others to quit.

Dealing with problems in the team can be difficult and it will vary a lot, but you should be able to notice what could be improved and most importantly, take actions whenever necessary.

## Conclusion

Building a great project or product is difficult and it takes time. If software engineering was precise and perfect we all would be out of our jobs.

Perfection is impossible, but you can work on multiple aspects to go in the right direction and build a great project, one that impacts people and does not drag the sanity of engineers.

There are times that a change of vision or direction in the project will be required to succeed. Every change must be propagated to the entire team or organization, you don't want people driving the project in the wrong direction due to miscommunication.

These are behaviors that I've seen or experienced multiple times, there is more, of course, but if you manage to keep what has been discussed in this article under control you will ensure that the project is going in the right direction, at least on the engineering side of it, bringing the correct idea to market is a whole new story.
