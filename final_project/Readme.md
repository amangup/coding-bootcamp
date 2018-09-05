# Final Project

In the final project, we will create an ebook reader web app which allows anyone to read books which we've made available (using books available in the free domain), and allow users to upload their own as well (as a stretch goal).

## Features

The web app allows both anonymous use and users with accounts to read books.

### Anonymous users

- They can see a global library of ebooks.
- They can read any book in that library in an online UI.

### Users with accounts

In addition to above features, creating an account leads to these additional benefits:

- They can create a personal library which is a selection of books from the global library (it's like starring the books they want to read).
- Whenever they read a book, the web app will synchronize their reading location. Whenever users come back to the web app later and read the same book, they will start reading from where they left off.
- (Stretch goal) Users can upload their own epub files, and that book is only visible in their own library.

### Design elements

The global libary of ebooks, or even personal libraries, can potentially include hundreds or even thousands of ebooks. Here are some suggestions which can make it easier to find what want to read:

- Navigation which uses the letters of the alphabet to help choose the book - either by the title, or by the author name.
- A search bar that finds books with that word in the title or in the author fields of the book.

## Implementation considerations

### E-book format

The web app will support the [ePUB e-book format](https://en.wikipedia.org/wiki/EPUB). This is a widely used format to store ebooks, and most books available to download online are shared in this format.

ePub format contains the _metadata_ of the book (title, author, etc.), and also includes the whole contents of the book formatted in a readable manner. We need to be able to extract that metadata, and also render the book in the browser. 

#### Reading ePUB metadata

I have included a file called `epub_metadata.py` in this folder which has an example code to extract the book details from the epub file. Note that it needs an external dependency `lxml` to be installed.

For all the ebooks on the web app, you will need to extract the metadata from the book and store in a DB table.

#### Rendering ePUB books

We will use the [Epub.js](https://github.com/futurepress/epub.js/) library to render ebooks. I have created an example web app which has the `read_book()` view. It uses the `read_book.html` template to render. The `render_template` call looks like this:

```python
return render_template("read_book.html", cfi=cfi_location, title=title, author=author,
                       book=url_for('static', filename='test.epub'))
```

- Everything should be obvious, except the parameter `cfi`, which we will discuss soon.
- There is a CSS file called `book.css` and some javascript in the template which makes this experience work.
  - Navigation of the book can be done by clicking on the arrows on the left and right, or using left and right arrow keys on the keyboard.
- I highly recommend that you run this web app `epub` and see how it works.
 
### Synchronizing read location

To implement this feature, we need to use AJAX. Periodically, the javascript in the page will find the location at which the user is in the book, and send a POST HTTP request to our web app. The web app must build a view to receive that request, and then update the location for that book in the user records.

The read location is encoded as an [ePUB Canonical Fragment Identifier](http://www.idpf.org/epub/linking/cfi/epub-cfi.html), or ePUB CFI. This is a string that identifies the exact the location in one specific book (it will not work on another book). It can look like this:

```
epubcfi(/6/2[item58]!/4/66[THE_OUTDOOR_LABORATORY]/2/1:387)
```

In the javascript code in `read_book.html` template, I have already implemented this mechanism which sends an update to the view `location_sync()`, every few seconds. The data sent (CFI string) is available in the `request.form["cfi"]` (ignore the fact that we are using `request.form` even though there is no form).

When opening a book to read, you can provide this CFI string as `cfi` parameter to the template. If the parameter is an empty string, then the book opens at the beginning.

### Uploading books

Look at [this section](https://github.com/amangup/coding-bootcamp/blob/master/lecture10/assignment_photo_filters.md#uploading-files) in the Photo filters assignment to learn how you can upload books.

## Deploying the website

When you are developing (and when its complete) keep deploying the website at PythonAnywhere.com to make sure everything works as intended. Make sure that use of HTTPS protocol is enforced.
