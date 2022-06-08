const assert = require('assert');
const Park = require('../models/park.js');
const Dinosaur = require('../models/dinosaur.js');

describe('Park', function () {

  beforeEach(function () {
    dinosaur1 = new Dinosaur('t-rex', 'carnivore', 50);
    dinosaur2 = new Dinosaur('stegasaurus', 'herbivore', 30);
    dinosaur3 = new Dinosaur('velociraptor', 'omnivore', 70);
    park = new Park('Jurassic Park', 25, []);
  });

  it('should have a name', function () {
    const actual = park.name;
    assert.strictEqual(actual, 'Jurassic Park');
  });

  it('should have a ticket price', function () {
    const actual = park.ticketPrice;
    assert.strictEqual(actual, 25);
  });

  it('should have a collection of dinosaurs', function () {
    const actual = park.dinosaurs;
    assert.deepStrictEqual(actual, []);
  });

  it('should be able to add a dinosaur to its collection', function () {
    park.addDinosaur(dinosaur1);
    const actual = park.dinosaurs;
    assert.deepStrictEqual(actual, [dinosaur1]);
  });

  it('should be able to remove a dinosaur from its collection', function () {
    park.addDinosaur(dinosaur1);
    park.addDinosaur(dinosaur2);
    park.addDinosaur(dinosaur3);
    park.removeDinosaur(dinosaur1);
    const actual = park.dinosaurs;
    assert.deepStrictEqual(actual, [dinosaur2, dinosaur3])
  });

  it('should be able to find the dinosaur that attracts the most visitors', function () {
    park.addDinosaur(dinosaur1);
    park.addDinosaur(dinosaur2);
    park.addDinosaur(dinosaur3);
    const actual = park.findMostAttractiveDinosaur();
    assert.deepStrictEqual(actual, dinosaur3)
  });

  it('should be able to find all dinosaurs of a particular species', function () {
    park.addDinosaur(dinosaur1);
    park.addDinosaur(dinosaur2);
    park.addDinosaur(dinosaur3);
    park.addDinosaur(dinosaur1);
    const actual = park.findDinosaurSpecies('t-rex');
    const expected = [dinosaur1, dinosaur1];
    assert.deepStrictEqual(actual, expected);
  });

  it('should be able to calculate the total number of visitors per day', function () {
    park.addDinosaur(dinosaur1);
    park.addDinosaur(dinosaur2);
    park.addDinosaur(dinosaur3);
    const actual = park.calculateVisitorsPerDay();
    assert.strictEqual(actual, 150);
  });

  it('should be able to calculate the total number of visitors per year', function () {
    park.addDinosaur(dinosaur1);
    park.addDinosaur(dinosaur2);
    park.addDinosaur(dinosaur3);
    const actual = park.calculateVisitorsPerYear();
    assert.strictEqual(actual, 54750);
  });

  it('should be able to calculate total revenue for one year', function () {
    park.addDinosaur(dinosaur1);
    park.addDinosaur(dinosaur2);
    park.addDinosaur(dinosaur3);
    const actual = park.calculateRevenuePerYear();
    assert.strictEqual(actual, 1368750);
  });

  it('should be able to remove all dinosaurs of a particular species', function () {
    park.addDinosaur(dinosaur1);
    park.addDinosaur(dinosaur2);
    park.addDinosaur(dinosaur3);
    park.removeAllDinosaursOfOneSpecies('t-rex');
    const actual = park.dinosaurs;
    const expected = [dinosaur2, dinosaur3];
    assert.deepStrictEqual(actual, expected);
  });

  it('should provide an object containing number of dinosaurs with each diet type', function () {
    park.addDinosaur(dinosaur1);
    park.addDinosaur(dinosaur2);
    park.addDinosaur(dinosaur3);
    const actual = park.dinosaurDietTypes();
    const expected = {
      carnivore: 1,
      herbivore: 1,
      omnivore: 1,
    };
    assert.deepStrictEqual(actual, expected)
  });

});
