title: Announcing podTo
date: 2018-02-06
author: Mark Steadman
tags: protocol

---

Subscribing to podcasts is hard. To prove it, try explaining it to someone with a new smartphone, who doesn’t know what an RSS feed is. Even if you have the default podcasting app on your phone (which is Apple Podcasts on iOS, and Google Play Music on Android, but only in America? Weird) you might not know that. What we need is a mailto: equivalent for podcasting. Which is why my friend and colleague [Brendan Hutchins](http://podcastadvocate.network/) came up with the podto: scheme, and I’m helping work out the technical stuff.

## The problem so far

Right now, there are a few options: you can just assume people are going to use iTunes (or Apple Podcasts) to subscribe. This is problematic as not everyone uses iTunes (not by a long chalk... yes, “long chalk” is a thing; leave me alone, I’m British).

Another option is to have a page which shows as many different podcast app icons as can comfortably fit on-screen. This makes it much harder for smaller or newer podcast apps to gain traction, as the easiest pathways are the already established ones. And as the overall listenership to podcasts increases, the app space is only going to get more fragmented. It’s also not a good user experience.

You could do some kind of smart device detection, where you try to sniff out what operating system the listener might be using, and best direct them to the right app. This is also a problem as those systems can’t tell what podcast apps you have in place, so for iOS they might default to Apple’s default podcast app, which many experienced podcast listeners don’t prefer.

The most democratic way of doing this is to provide an RSS URL. But that presupposes people know what one of those is, or how to get their podcast player to use one (assuming the podcast player is legitimate, and accepts RSS URLs... we’ll get onto that later).

## Our proposed solution
Subscribing to a podcast should be as easy as sending an email, if not easier. In an ideal world, you find a podcast you like, somewhere on the web, click “Subscribe” and are redirected to your podcast app of choice, which shows the artwork, description and list of episodes (just as if you’d tapped a search result within the app). You tap the “Subscribe” button in your app, and you’re done.

### Why have another Subscribe button inside the app?
It seems sensible to have a layer of confirmation in-between tapping the initial link and then subscribing, in case you tapped the link by accident and weren’t sure what would happen. Alternatively, for feeds that require a username and password, this prompt can potentially be given when the user hits the Subscribe button in-app.

## The structure of the URL
At its heart, a podto: URI is just an RSS feed URL with the http: or https: portion replaced with podto:. So, for the [Platform](https://platform.podiant.co/) podcast I record with Brendan, our RSS URL is http://feeds.podiant.co/platform/rss.xml, so our podTo URI would be podto://feeds.podiant.co/platform/rss.xml

## The user experience
Our proposal is that app developers build podto: support into their software. This isn’t all that complex; both Android and iOS support custom URI schemes, and there’s no inherent restriction regarding multiple apps using the same URI scheme (a little on that later, also).

We envisage podto: links working just like normal, everyday links to email addresses and other things on the Web. A user clicks a Subscribe link, their device prompts them if they want to open the link in their installed podcast client, they say “yes” and are redirected to the app to subscribe. Couldn’t be simpler.

## The challenge ahead
Implementing this is a technically trivial task. Its difficulty lies in asking everyone with a stake in the industry to come together for its betterment. If we all support it, we make the podcast experience better for everyone. The easier it becomes to subscribe to podcasts, the more people will.

While it would be great to have Apple adopt the podto: standard, their current model precludes anyone else from using a “built-in” URI scheme if Apple already provides support for it. This would present Apple with a grossly unfair advantage over third-party podcast app developers, as no other iOS apps would be able to respond to the URI scheme, so we’d be keen to work with Apple on waiving the built-in URI scheme lockdown for this case (if the Apple Podcasts app is hidden from the home screen).

We also have a tricky chicken-and-egg problem to negotiate. App developers need to know that it’s worth building support for this URI scheme into their apps, which means web developers need to add support in, but if not enough apps support it, the experience for the user will be a scary error message.

I’m exploring a JavaScript library or drop-in script that will attempt to sniff out whether the podto: scheme is supported by the browser, or simply show a friendly message if the browser doesn’t seem to have done anything useful with the URL after a second. This can then show a list of players that currently support the podto: URI scheme, and point to resources on this website for how to subscribe to podcasts (preferably without being tied to specific podcast apps, so that we don’t play favourites).

## A quick note on RSS, JSON Feed and things that aren’t podcasts
A podcast is only a podcast if it has an RSS feed. Otherwise it’s just some audio on the Internet. Still as engaging, entertaining and worthwhile as a podcast, but /not/ a podcast. So this scheme is only reserved for podcasts (audio or video programs that syndicate their content using the open RSS), which currently excludes services like Spotify and Audible, but does include private feeds provided by the likes of Patreon.

In the future, we should look at allowing JSON Feed URLs to be specified in the same way. This involves a little more work on the part of the app developer (as the podto: URI won’t communicate whether an app uses XML or JSON), but it could be a worthwhile exercise.

## Join us!
If you build apps, websites or services around podcasting, if you run the website for your own podcast, or you just love the open web, get in touch. <joinus@podto.org> is the best place to start. We’d love to have you on board so we can make podcasting as easy for listeners as it should be.
