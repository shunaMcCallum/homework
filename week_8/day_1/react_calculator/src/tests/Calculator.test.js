import React from 'react';
import Calculator from '../containers/Calculator';
import { render, fireEvent, getByTestId } from '@testing-library/react';

describe('Calculator', () => {
  let container;
  let button1;
  let button2;
  let button3;
  let button4;
  let button5;
  let button7;

  let buttonAdd;
  let buttonEquals;
  let buttonSubtract;
  let buttonMultiply;
  let buttonDivide;

  let clear;
  let runningTotal;


  beforeEach(() => {
    container = render(<Calculator />)
    button1 = container.getByTestId('number1');
    button2 = container.getByTestId('number2');
    button3 = container.getByTestId('number3');
    button4 = container.getByTestId('number4');
    button5 = container.getByTestId('number5');
    button7 = container.getByTestId('number7');

    buttonAdd = container.getByTestId('operator_add');
    buttonEquals = container.getByTestId('operator-equals');
    buttonSubtract = container.getByTestId('operator-subtract');
    buttonMultiply = container.getByTestId('operator-multiply');
    buttonDivide = container.getByTestId('operator-divide');

    clear = container.getByTestId('clear');
    runningTotal = container.getByTestId('running-total');

  })

  it('should change running total on number enter', () => {
    fireEvent.click(button4);
    expect(runningTotal.textContent).toEqual('4');
  })

  it('should add two numbers together', () => {
    fireEvent.click(button1);
    fireEvent.click(buttonAdd);
    fireEvent.click(button4);
    fireEvent.click(buttonEquals);
    expect(runningTotal.textContent).toEqual('5');
  })

  it('should subtract one number from another', () => {
    fireEvent.click(button7);
    fireEvent.click(buttonSubtract);
    fireEvent.click(button4);
    fireEvent.click(buttonEquals);
    expect(runningTotal.textContent).toEqual('3');
  })

  it('should multiply two numbers together', () => {
    fireEvent.click(button3);
    fireEvent.click(buttonMultiply);
    fireEvent.click(button5);
    fireEvent.click(buttonEquals);
    expect(runningTotal.textContent).toEqual('15');
  })

  it('should divide one number by another', () => {
    fireEvent.click(button2);
    fireEvent.click(button1);
    fireEvent.click(buttonDivide);
    fireEvent.click(button7);
    fireEvent.click(buttonEquals);
    expect(runningTotal.textContent).toEqual('3');
  })

  it('should concatenate multiple number button clicks', () => {
    fireEvent.click(button5);
    fireEvent.click(button5);
    fireEvent.click(button5);
    expect(runningTotal.textContent).toEqual('555');
  })

  it('should chain multiple operations together', () => {
    fireEvent.click(button1);
    fireEvent.click(buttonAdd);
    fireEvent.click(button2);
    fireEvent.click(buttonEquals);
    fireEvent.click(buttonMultiply);
    fireEvent.click(button5);
    fireEvent.click(buttonEquals);
    expect(runningTotal.textContent).toEqual('15');
  })

  it('should clear the running total without affecting the calculation', () => {
    fireEvent.click(button4);
    fireEvent.click(buttonMultiply);
    fireEvent.click(button5);
    fireEvent.click(buttonEquals);
    fireEvent.click(clear);
    fireEvent.click(buttonAdd);
    fireEvent.click(button5);
    fireEvent.click(buttonEquals);
    expect(runningTotal.textContent).toEqual('25');
  })
})

