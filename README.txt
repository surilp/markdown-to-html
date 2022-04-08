Steps to convert markdown to html:

1) python main.py
2) Type in or paste the markdown
3) Type 'convert' to convert typed/pasted markdown to html
4) Continue step 2 to 3 as many times as you wish
5) Once done type in 'quit' to exit


Sample execution of the main.py is below:

Type in or paste markdown
Type in "convert" to get html
Type in "quit" to exit
-----------Start of User Input(Markdown) ------------------
# Sample Document

Hello!

This is sample markdown for the [Mailchimp](https://www.mailchimp.com) homework assignment.
convert
-----------End of User Input(Markdown) --------------------
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
-----------Start of Output(HTML) ------------------
<h1>Sample Document</h1>

<p>Hello!</p>

<p>This is sample markdown for the <a href="https://www.mailchimp.com">Mailchimp</a> homework assignment.</p>
-----------End of Output(HTML) ------------------
Type in or paste markdown
Type in "convert" to get html
Type in "quit" to exit
-----------Start of User Input(Markdown) ------------------
# Header one

Hello there

How are you?
What's going on?

## Another Header

This is a paragraph [with an inline link](http://google.com). Neat, eh?

## This is a header [with a link](http://yahoo.com)
convert
-----------End of User Input(Markdown) --------------------
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
-----------Start of Output(HTML) ------------------
<h1>Header one</h1>

<p>Hello there</p>

<p>How are you?
What's going on?</p>

<h2>Another Header</h2>

<p>This is a paragraph <a href="http://google.com">with an inline link</a>. Neat, eh?</p>

<h2>This is a header <a href="http://yahoo.com">with a link</a></h2>
-----------End of Output(HTML) ------------------
Type in or paste markdown
Type in "convert" to get html
Type in "quit" to exit
-----------Start of User Input(Markdown) ------------------
quit
Thank you for using the converter