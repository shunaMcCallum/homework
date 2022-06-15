import React, { useState } from 'react';

// here we pass our onCommentSubmit instruction from the CommentBox as a prop - we can now use this below
const CommentForm = ({onCommentSubmit}) => {

    const [author, setAuthor] = useState("");
    const [text, setText] = useState("");

    const handleAuthor = (event) => {
        setAuthor(event.target.value);
    }

    const handleText = (event) => {
        setText(event.target.value);
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        // trim removes any whitespace at the end of a string - just in case a user accidentally inputs an extra space at the end of their input, or even just a space on its own
        const newAuthor = author.trim();
        const newText = text.trim();
        // now we want to set this up so that the input fields have to be filled in to submit the form:
        if (!newAuthor || !newText) {
            return
        }
        // here is where previously we updated our data by creating the copy list etc. - BUT remember we cannot update and pass NEW data back up to the level above in our hierarchy, 
        // so we need to do things differently - we need to go up to the level above and write the function to grab our data in there
        // now we set up our new comment variable to grab the data, then call on the function we were passed from the CommentBox level above in order for that level of our program to grab the data
        // instead of this one
        const newComment = { author: newAuthor, text: newText, id: Date.now() }
        onCommentSubmit(newComment)
        // remember to set your input fields back to blank after the submit has been completed - this is the final thing to do whenever you have a form input
        setAuthor("");
        setText("");
    }

    return (
        // adding onSubmit here will tell our app what to do with the data after it's been submitted
        <form onSubmit={handleSubmit}>
            <label htmlFor="author">Author: </label>
            {/* adding a value to our input field allows us to track the state, i.e. take in the new value created by this form */}
            {/* adding onChange then will attach our function which will allow us to actually change/input this data by setting up what happens when we type something in */}
            <input required type="text" placeholder="Author" id="author" value={author} onChange={handleAuthor} />
            <label htmlFor="text">Text: </label>
            {/* adding required to our input helps to ensure that these fields have to be filled in and cannot be left blank in order for the form to be submitted */}
            <input required type="text" placeholder="Say something..." id="text" value={text} onChange={handleText} />
            <input type="submit" value="Post Comment" />
        </form>
    )

}

export default CommentForm;