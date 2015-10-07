Title: Nunjucks eval tag
Date: 2015-07-11 08:00
Modified: 2015-07-11 08:00
Tags: nunjucks, eval, jinja2, NodeJS
Slug: nunjucks-eval

This week I started to work in [Gistfy project](https://github.com/alexandrevicenzi/gistfy) again, and one of the changes is replace [swig](https://github.com/paularmstrong/swig) by [Nunjucks](http://mozilla.github.io/nunjucks/). [swig is no longer maintained](https://github.com/paularmstrong/swig/issues/628), and Nunjucks looks a really cool project.

I like Nunjucks because it has a Django like template engine. In fact, Nunjucks is a [port of Jinja2](http://mozilla.github.io/nunjucks/templating.html#templating). [Jinja2](http://jinja.pocoo.org/docs/dev/) is a Python template engine.

Nunjucks is very simple to use and has a lot of filters and tags in it, if you're a Django user it will be very easy to create something with it. In fact, I created an *evil* extension to allow me to eval some JS code.

This all started because I needed to put the current year in my page. I could use JS in browser or use a variable and pass through render to do this. But no, I decided to eval the code using a template tag. Well, there's no tag for this, I think, so I built one.

It's very simple to use the tag and looks like [set](http://mozilla.github.io/nunjucks/templating.html#set) tag.

In the server:

```js
var nunjucks = require('nunjucks'),
    njeval = require('nunjucks-eval'),

var env = nunjucks.configure({ autoescape: true });

njeval.install(env);
```
And then in the view:

```
{% eval year="new Date().getFullYear()" %}
<span>{{ year }}</span>
```

You can check the [source code of nunjucks-eval](https://github.com/alexandrevicenzi/nunjucks-eval), it's very simple and small.
