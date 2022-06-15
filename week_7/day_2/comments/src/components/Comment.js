import React from 'react';

// example of passing props down from the level above:
// In line 7 we are setting up our component's parameters - when this becomes an argument, it'll pull the props we hard-coded into CommentList
// this works fine for smaller apps where you won't have many props - but for bigger ones we'll be working with a lot more data which will be come difficult to track
// const Comment = (props) => {

//     return (
//         <>
//             {/* props is are objects in React so we can access our data points by using the . operator as below */}
//             <h4>{props.children}</h4>
//             <p>{props.author}</p>
//         </>
//     )

// }

// above we've been able to access specific data points in our props by using the . operator, however we can save ourselves from having to do this
// to do this we use destructuring - instead of passing a whole prop into our component as an argument, we destructure it and pass each data point
// the syntax for setting this up is shown below - we use {} in the case of an object to pull out particular pieces data on each prop
// const Comment = ({ children, author }) => {
    
//     return (
//         <>
// and here we can just say that we want to display children and author without needing to attach the prop object each time
//             <h4>{children}</h4>
//             <p>{author}</p>
//         </>
//     )

// }


// below, now working with the prop data that's been passed from the level above - we pass comment in curly braces into our function, as
// props are passed in like arguments, and this pulls the individual comment prop that we created in the CommentList file
const Comment = ({ comment }) => {

    return (
        <>
            {/* now we can use the dot operator to access each individual piece of data attached to our props objects */}
            <h4>{comment.text}</h4>
            <p>{comment.author}</p>
        </>
    )
}

export default Comment;