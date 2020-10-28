---
title: Is my project failing?
date: 2020-08-05
slug: is-my-project-failing
description: Failure can come in many forms and shapes, but there are usually signs along the way that will help you fix it before being too late.
summary: In today's article, I'm going to talk about what I've seen over the years. Things that slowly contributed to the failure of a project and how to avoid it.
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

Failure can come in many forms and shapes. I've seen a company work on two major projects for years that never launched. An interesting project that lost all the good engineers due to bad management. Difficult and expensive project maintenance. Tools and technologies from over 10-15 years ago used in production, and more.

Yet, none of these companies has filed for bankruptcy. The companies are still there, profitable, I think. This means that sometimes failure is not a total disaster, but it may set you back.

In today's article, I'm going to talk about what I've seen over the years. Things that slowly contributed to the failure of a project and how to avoid it.

## Being fast instead of Agile

Agile is a way to quickly interact, adapt, or change. It also means that you usually have fast deliverables because you work in iterations. Delivering small pieces that work from time to time. In the end, the entire project can still take hundreds of hours for completion.

You should think of Agile as a development mindset. A way of dealing with requirements, changes, and all bumps that you will find while working on a project. Agile is not a way to deliver a project in less time possible.

## Scarce documentation

The lack of documentation introduces many problems, from development to customer support. In engineering, there's a thought that documenting things is a waste of time. Someone can read the code and understand right? Yes. One can understand what the code is doing by looking at it. No one is going to magically figure out why it is that way, or what was the business idea behind it.

Documenting code, architecture, and all other bits and pieces are good for developers. It will save you time once a problem appears as there's something in place to understand the why's.

No less important, documentation for customers/users is equally or more important. The lack of proper documentation will be a burden for your support team. Proper documentation and a knowledge base are important for users. When users can't solve problems by themselves, they open a ticket and that costs money.

## Poor test coverage

TDD, BDD, DDD, unit test, integration test, load/stress test, E2E, the list goes on. Yes, it seems an overload of testing methods and practices, but everything has its place and time. I'm not going to discuss the differences between each. You should know that testing is as important as coding new features.

Testing your product is the easiest and cheapest way to find bugs. It's the easiest because a bug can be quite costly, timely and monetary, to fix once it's in production. It's cheap because a bug can impact your product in production and this can impact your revenue.

There's no rule for too much testing. The biggest the coverage the more confident you can be with new releases. Yes, testing it properly takes time, but it also saves time in the future.

## Wrong tooling

Choosing the wrong tools for the job is a problem. C++ for web development works, but is it the right tool? Probably not. There are programming languages and frameworks more suitable for this scenario.

There may be a range of tools for a particular problem. Finding something that the team is capable of maintaining is the safest bet. You don't want to choose Perl and figure out later on that it is difficult to find skilled people in this particular language.

Using the latest bleeding-edge framework that someone wrote over one night, posted on Hacker News, and got 10k stars on GitHub in a single day is also something that you should avoid. Tooling with a great community around can easily come in handy once you need help.

## Wrong size

Premature optimization is the root of all evil. This is a famous saying among software engineers, and it's credited to Donald Knuth. Yes, premature optimization can be bad. You can probably predict the growth of your project. It should be possible to scale it if required, with minimal effort, at least to some extent.

You can build an amazing project, but if the project can't keep up with its user base that's going to be a big problem. I'm pretty sure that you don't want to rewrite something entirely after three months of the launch.

Predicting if a project will go viral is impossible. But you can still predict the project growth for the next six months or two years in most cases. If you can, great. Make it in a way so future changes can be accommodated with ease, but don't implement until it's required.

## Not listening to developers

Who understands the project better than the ones that wrote it? Listening to their concerns is important. Taking actions once they notify things that do not seem right is strongly advised.

Developers will come with scale and maintenance concerns. They will ask for time to work on things that won't deliver anything valuable for customers at first glance. What people don't understand is that there's a hidden cost to keep services up and running.

Would you rather deliver a new feature or work on tasks to keep all systems operational? Finding time for maintenance and updates is also important.

## Lack of understanding

Understanding customers and/or stakeholders can be hard. That's why you need to invest time in requirements and also validate it before any work starts.

Building the wrong set of features as you know can be catastrophic. Building the correct requirements that were poorly described and do not fit any use case is as bad as it.

Requirements may not be enough to fully capture someone's idea or vision. Thus, good communication and fast iterations for prototypes can be crucial to success.

## Rushing too much

Everyone wants to deliver things ASAP these days. Rushing releases to the point that it delivers a low-quality software is the worst that you can do.

Faulty software causes customers and users to lose trust. It can also lead them to competitors or alternatives. I would rather release something that has fewer features but works than a gigantic piece that does not.

## Imbalance

A team must be in harmony most of the time. Constant drama and divergences can affect project quality, readiness, timelines, and more.

Dealing with problems in the team can be difficult, and it will vary a lot. You should be able to notice what could be improved, as well as take action whenever necessary.

## Conclusion

Building a great project or product is difficult, and it takes time. If software engineering was precise and perfect, we all would be out of our jobs.

Perfection is impossible. You can work on many aspects to go in the right direction and build a great project. A project that delivers great value for customers and does not drag the sanity of engineers.

There are times that a change of vision or direction in the project will be required to succeed. Every change must be propagated to the entire team or organization. You can avoid the project going in the wrong direction due to miscommunication.

These are behaviors that I've seen or experienced many times. There is more, of course. If you manage to keep what has been discussed here under control, you will ensure that the project is going in the right direction. At least on the engineering side of it, bringing the right idea at the right time to market is a whole new story.
