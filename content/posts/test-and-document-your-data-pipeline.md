---
title: Test and document your data pipeline
tagline: Good programming practices are necessary for every project
date: 2020-10-16
slug: test-and-document-your-data-pipeline
description: While working on a given project, we thought that testing a data pipeline was difficult, and we always postponed the test of some areas. Later on, we learned the consequences of not testing it.
summary: While working on a given project, we (as a team) thought that testing a data pipeline was difficult, and we always postponed the test of some areas. Later on, we learned the consequences of not testing it.
images:
  - /images/content/bug.png
tags:
  - engineering
  - good-practices
  - data-processing
  - tests
  - documentation
---

{{< figure src="/images/content/bug-t.png" alt="Bug" width="300" caption="Image by [Eezy](https://www.iconfinder.com/Vecteezy)" >}}

The article [Unit Test Your Data Pipeline, You Will Thank Yourself Later][unit-test-pipeline] on [KDnuggets][kd] caught my attention because we learned this the hard way.

While working on a given project, we (as a team) thought that testing a data pipeline was difficult, and we always postponed the test of some areas. Later on, we learned the consequences of not testing it.

Everyone knows that the lack of tests in your code leads to bugs and behavior that no one fully understands. Testing is a small part of the software development process that should be always considered.

There were two main issues in our project:

- Hidden bugs due to low test coverage
- Lack of understanding of how things worked due to lack of documentation

Software development is not perfect, bugs will appear from time to time, but you can reduce the chances by testing your code.

New team members need to start somewhere and current ones need to keep in sync with everything that is going on. The easiest way to accomplish that is by documenting your code, requirements, user stories, and everything in between.

These issues became more apparent once we found a critical bug. Data went missing in our pipeline, some service was losing data, but we had no clue why or where. The output result was, of course, inaccurate, showing less information than what it should.

Luckily, we had tracing and logging. We managed to pinpoint a path between two services. The bug was in one of them, exactly where we had to find yet. It took us a lot of time to discover it, but after looking at the code of the most likely service, we found the bug. It was a silly one, some data was being overridden while loaded by an aggregator function.

The solution was easy I would say, but we learned our lesson in a hard way. There are many areas in a data pipeline that are basic operations that can and should have test coverage.

This data pipeline made many data transformations with Pandas. In fact, the ML part was tiny if compared to the other services. [Pandas][pandas] is predictable, given an input and a set of operations it should produce an output. The difficult part was the data used as input. It's usually a lot more than single values. We had to prepare the DataFrames, and this was somewhat challenging, with big payloads to test a simple operation. It's doable, but a bit more complex than your regular unit testing.

I would also say that you can test your model to some extent as well. Training it with a given dataset and using another one for validation is one form of ensuring that it works as expected, or perhaps testing the accuracy of the model in some cases.

It does not matter the type of project you are working on, there are basic items that should exist for a project:

- Documentation
- Test coverage
- Logging
- Tracing
- Monitoring

The benefits of such items are unmeasurable, and everyone in the team will be thankful once a bug emerges.

[kd]: https://www.kdnuggets.com/
[unit-test-pipeline]: https://www.kdnuggets.com/2020/08/unit-test-data-pipeline-thank-yourself-later.html
[pandas]: https://pandas.pydata.org/
