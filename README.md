# Truffle Pig

Search/replace html truffle.

Truffle pig makes it easy to find what you're looking for in HTML documents and replace it with something else, or nothing at all.


## Philosophy

Truffle pig wants to find exactly what you want (using CSS selectors), but also there insert (or replace, append, prepend, insert before or after) any text you would like.


## Example Usage

Say we have this example HTML document:

```html
<!-- index.html -->

<html>
<head>
  <title>Good Reads Here</title>
</head>
<body>
  <nav>
    <h1>A Peculiar Heading</h1>
  </nav>

  <article>
    <p>
      Lorem ipsum dolor sit amet, why don't you just read something 
      more interesting?
    </p>
  </article>
  
  <article>
    <p>Apple pie is delicious.</p>
  </article>
</body>
</html>
```

And we don't like the title of the page. Instead of going into the file and editing it by hand, we can use our truffle pig!


```
trufflepig -i 'Best Reads Here, Ever' 'head title' index.html
```

Which, predicably, changes the title of the document, in place.

But that's not too interesting, is it? How about changing the title of a number of documents?

```
trufflepig -i 'Good Reads Here' 'head title' *.html
```

What about replacing the navbar we have on all of these pages with a better one? Given this file: 

```html
<!-- navbar.txt -->
  <h1>A Masterful Heading</h1>
  <ul id="good-list">
    <li>An item.</li>
    <li>A second item.</li>
  </ul>
```

Certainly:

```
trufflepig 'body + nav' *.html < navbar.txt
```

And then let's add a subheader right after that `h1`!

```
trufflepig -i '<h2>Really, the above is excellent</h2>' --after 'nav h1' *.html
```


## Help (-h) output

```
usage: trufflepig.py [-h] [-i text] [--dry] [--replace] [--remove] [--append]
                     [--prepend] [--after] [--before]
                     selector [output files) [output file(s ...]]

Search/replace html truffles.

positional arguments:
  selector              css selector to search for (JQuery syntax)
  output file(s)        file to modify

optional arguments:
  -h, --help            show this help message and exit
  -i text, --input text
                        text with which to replace selection with
  --dry                 instead of modifying the input files, print results of
                        the transformation
  --replace             (default) replace selection
  --remove              remove selection
  --append              insert inside selection, after existing content
  --prepend             insert inside selection, before existing content
  --after               append to selection
  --before              prepend to selection

For more information, check http://github.com/ihodes/trufflepig.
```
