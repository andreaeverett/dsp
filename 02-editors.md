# Choose and learn your editor(s)


Computing's interface is text. To work effectively, you need to be fluent with this interface.


### Typing

It may sound silly, but [make sure](http://www.typingtest.com/) you know how to type. You should be comfortable typing with perfect accuracy at 60 words per minute, at least. If you currently can't, practice until you can.

A lot of your work will be done in a text editor. You have to know how to use your editor. Any editor will work, but knowing a powerful editor well will make you faster, more comfortable, and more effective.

---

### Terminal Editor

Sometimes you will need to use a non-graphical text editor. This means an editor that will run entirely inside a terminal window, without spawning a new window, entirely without mouse input.

Make sure that you know at least one of these well enough to do basic editing in a terminal:

 * Emacs
 * vim
 * nano

You should know at least enough vim to be able to get out of it, because it is the default on many systems and you might find yourself in it even if you didn't mean to be.

If you intend to use a graphical editor that doesn't run in a terminal, nano might be a good choice for you because it is very simple.

Both Emacs and vim have built-in interactive tutorials that you can try.


---

###Graphical Editor

You will probably spend most of your time with access to a graphical interface, where you have more choices in editors and integrated development environments.

Popular editors and IDEs include:

 * Emacs
 * vim
 * Sublime
 * Atom
 * Spyder
 * PyCharm
 * [Rodeo](http://blog.yhat.com/posts/introducing-rodeo.html)

If you choose Emacs or vim, you will have essentially the same editor experience across graphical and non-graphical environments, which is nice. It's also nice to be able to work without ever having to use a mouse. Emacs and vim have somewhat steep learning curves, but they give you the ability to customize your environment quite a lot to make it exactly what you want.

Sublime is probably the most popular editor for new coders. You can set it up to integrate with Python fairly well. Atom is pretty similar to Sublime but has an interesting open architecture and is developed by folks at GitHub.

Spyder and PyCharm are IDEs for Python. They try to give you a fully configured setup out of the box.

We will also use Jupyter (IPython) notebooks, but this does not remove the need for proficiency in an editor or IDE.

---

###Q1. Terminal Editor

**What terminal editor will you use? How did you make your decision?**

I am going to use vim.  Since I’ve never used any of the three before and you say I need to have at least a basic competency in vim, I think it makes the most sense to focus on that one.  Although it sounds more difficult than nano, it also sounds as if I can learn enough to do some basic things and then learn more later if it becomes clear that doing so would be useful.  I completed the vim tutorial.

--

###Q2. Graphical Editor

**What graphical editor will you use? How did you make your decision? What are some interesting features of your editor? What are some useful keyboard shortcuts for your editor? How do you customize your editor?**

**What graphical editor will you use? How did you make your decision?** 

I have been using TextWrangler, but after looking at some of the other suggestions here I am going to start working with Atom and trying to get comfortable with it.  From what I’ve read Atom and Sublime are similar but the former is free and I like the idea of being able to access packages written by other users if they look like they will come in handy.  As for Emacs and Vim, I don’t think I have enough coding experience to use those for all of my coding needs at this point, given their high learning curve.  Further, while it seems likely that I might want to learn one of the IDEs at some point, for now I think I will be more comfortable with a simpler environment with just one window to focus on at a time.

**What are some interesting features of your editor?**  

1. This might be standard among the fancier text editors, but it was new to me: When I open a bracket or a parenthesis or a curly brace, it automatically creates a closing one for me.  That’s pretty neat.  

2. Another thing that looks neat is that I can create ‘snippets’ that will basically serve as saved shortcuts to generate specific blocks of text.  This looks like it could be useful for things I type a lot.

3. It supports the syntax for many different languages.  For instance, it appears I can use it for files in python but also SQL.

4. In my Terminal, if I want to create a new file and open it in Atom, I can type ‘atom newfile’ instead of ‘touch newfile’ and it will create and open the new file in Atom automatically.  This seems like a handy feature for sure.

**What are some useful keyboard shortcuts for your editor?**

cmd-R : When you are in a file, this pulls up a list of methods / functions in the file and lets you choose one to jump to.

cmd-P: Lets you search for a file by name from within the text editor window.

cmd-shift-P : It brings up the command palette, which lists every Atom command.  You can search there as well.

cmd-e : Find-and-replace, using the highlighted selection as the ‘find’ pattern.

ctrl-g : Lets you enter a specific line number to jump to.

ctrl-m : If my cursor is at a bracket or curly brace or parenthesis, this will move it to the matching one.

ctrl-shift-L : Brings up a menu to select which language (grammar) you are using for the currently open file

**How do you customize your editor?**

I’m sure there are more things that I could customize than I have done so far.  But an obvious one is the choice from among several themes (under Settings —> Themes), which set the background and text colors for both the UI and the syntax inside the editor.  The basic choice appears to be between a light background with dark text or a dark background and higher text colors, although there are variations on each of these.  Another way to customize it is that you can disable individual packages under Settings —> Packages.  For instance, I disabled one that sends certain information about my usage of Atom to Google Analytics.  
