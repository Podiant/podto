title: The anatomy of a podTo URI
date: 2018-02-22
author: Mark Steadman
tags: protocol

---

After hearing people’s concerns, I’ve elected to change the URI format a little, making it a little more verbose but much more flexible. The new pattern for podto URIs looks like this:

`podto:url=<url>&[type=<type>]&url=<url>&[type=<type>]...`

Where

* `url` is the fully-qualified URL of the podcast feed
* `type` (optional) is the type of feed. Possible types include:
	* `application/xml+rss`
	* `application/json`
	* `application/json+dotpodcast`

Everything after the `podto:` part needs to be ISO encoded, so the URI can be easily parsed.

## The `url` field

Instead of just replacing the “http” part of a URL with “podto”, I’m now suggesting we ISO-encode the entire URL of the RSS feed. That way, we can support HTTP and HTTPS feeds without apps needing to do any extra work.

## The `type` parameter

If no `type` parameter is specified, we should always assume it’ll be `application/xml+rss`.

### `application.json`

This gives apps the option to support JSON Feeds if they want.

### `application/json+dotpodcast`

This is a feed format set out by the [DotPodcast](https://dotpodcast.co/) project (there will likely be more on that story at a later date).

## Repeating parameters

I’m suggesting we allow the `url` and `type` parameters to be repeated so that multiple formats of a feed can be specified, and the receiving app can choose which format it prefers (for example, going forward we might want to prefer JSON Feed content, as it’s much easier to parse, but fall back to RSS if JSON isn’t available on a particular feed).

When doubling or tripling up on parameters, the order matters. The tope should not be inferred by the URL, so the `url` parameters need to be in the same order as the `type` parameters.

## podTo on the web

We can’t currently add `podto:` as a URI scheme on the web for desktops, as that would require people to install apps that can receive the URI. That’s fine on mobile - and is, in fact, the entire point - but on the web in desktops, we’re going to use `web+podto:` for now.

I’m looking to build a JavaScript button - or a simple script that can be attached to any HTML link or button element - that will try and detect which protocol to use, as `web+podto:` can’t be handled by iOS (there’s no mechanism for registering custom namespaces on mobile Safari).

## Next steps

There’s a [testing dingus](https://dingus.podto.org/) available for you to try, which will ask if you want to register the tool to accept podTo links. If registration succeeds, you should move on to the next step where you can test a specific RSS URL. When you click the “Subscribe” button, your browser should take you to step three. From there on - even if you get an error message - the process works, and you’ve proven that your browser is able to accept links using the podTo URI scheme.

This won’t work on mobile yet, because of the reasons I listed above, so our next goal is to get some mobile app support around the `podto:` URI scheme.

Exciting times!
