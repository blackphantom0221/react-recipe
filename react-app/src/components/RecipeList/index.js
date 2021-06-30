import React, { useEffect, useState } from "react";
import { getAllRecipes } from "../../store/recipes";
import { useDispatch, useSelector } from "react-redux";

const RecipeList = () => {
  const dispatch = useDispatch();
  const allRecipes = useSelector((state) => state.recipeReducer.recipes);

  const getAllRecipesFunction = async () => {
    await dispatch(getAllRecipes());
  };

  useEffect(() => {
    console.log("this is in the useEffect");
    if (allRecipes === null) {
      getAllRecipesFunction();
    }
  }, [allRecipes]);

  return (
    <div>
      <h1>Recipe List</h1>
      {allRecipes?.map((recipe) => {
        return [
          <h1>{recipe.name}</h1>,
          <p>{recipe.description}</p>,
          <img src={recipe.image}/>,
          <p>{recipe.servings}</p>,
          <p>{recipe.time}</p>,
          <p>{recipe.instructions}</p>,
          <button onClick={() => console.log('I have been clicked', recipe.id)}>Edit</button>
        ];
      })}
    </div>
  );
};

export default RecipeList;
