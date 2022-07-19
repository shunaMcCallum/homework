import React from 'react'

const DropDown = ({categories, onCategorySelect} ) => {

    const handleSelect = (event) => {
        event.preventDefault();
        const chosenIndex = event.target.value;
        const chosenCategory = categories[chosenIndex];
        onCategorySelect(chosenCategory);

    }

    const categoryItems = categories.map((category, index) => {
        return <option key={index} value={index}>{category.name}</option>
    })
   
    return (
        <select onChange={handleSelect}>
            <option selected disabled value="">Select a Category</option>
            {categoryItems}
        </select>
    );
}

export default DropDown;