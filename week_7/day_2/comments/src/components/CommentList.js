import React from 'react';
import Comment from './Comment.js'

// const CommentList = () => {

//     return (
//         <>
// below we've hard-coded some data in - we wouldn't normally do this but it's useful to see how it would be done
// in this example our author is a prop, and then the comment is a child of that prop - we would normally only include the prop when we don't use hard-coded data
// so this was an example of passing hard code from our CommentList to our Comment component - below shows how it flows through from the top level
//             <Comment author="Rick Henry">React is cool!</Comment>
//             <Comment author="Val Gibson">I'm dreaming in React...</Comment>
//         </>
//     )

// }


// here's how we pass our comments through from the level above as a prop - we put comments in curly braces because we're taking specifically the
// comments prop that we named in our CommentBox file
// remember that CommentList has no state, just the data it has been given by the CommentBox - i.e. the comment objects
// we're going to now map the array of comment objects into an array of Comment components - i.e. data that our Comment file can work with
const CommentList = ({ comments }) => {
    
    // now we're setting up our function that will loop over the comments prop array that was passed in on line 22
    const commentNodes = comments.map((comment) => {
        return (
            // when we set up what data will be returned by this function, we need a unique identifier (key) for each component
            // this is because React only ever re-renders specific data points when they change, rather than having to re-render everything on a
            // page - so we can use something like an id number (as we'll inevitably end up with when we get to databases) to allow React to do this
            // note, below we have again declared the name of our prop which will be passed down in green as "comment" and set it equal to each comment 
            // obect we're mapping out
            <Comment comment={comment} key={comment.id} />
        )
    })
    // so we now have an array of Comment components called comment Nodes

    return (
        <>
            {/* this was the hard coded version from earlier */}
            {/* <Comment author="Rick Henry">React is cool!</Comment>
            <Comment author="Val Gibson">I'm dreaming in React...</Comment> */}

            {/* now we can just put in the result of our commentNodes function - note we no longer need the ul and li elements */}
            {/* note that this is pulling the data from our commentNodes function created above - so it's pulling each individual comment
            object which can now be passed down to the comment component */}
            {commentNodes}
        </>
    )

}



export default CommentList;