const Park = function (name, ticketPrice) {
    this.name = name;
    this.ticketPrice = ticketPrice;
    this.dinosaurs = [];
};

Park.prototype.addDinosaur = function (dinosaur) {
    this.dinosaurs.push(dinosaur);
};

Park.prototype.removeDinosaur = function (dinosaur) {
    const listIndex = this.dinosaurs.indexOf(dinosaur);
    this.dinosaurs.splice(listIndex, 1);
};

Park.prototype.findMostAttractiveDinosaur = function () {
    // const value = this.dinosaurs.reduce((max, obj) => (max.guestsAttractedPerDay > obj.guestsAttractedPerDay) ? max : obj);
    // return value;
    let value = this.dinosaurs[0];
    for (let dinosaur of this.dinosaurs) {
        if (dinosaur.guestsAttractedPerDay > value.guestsAttractedPerDay) {
            value = dinosaur;
        };
    };
    return value;
};

Park.prototype.findDinosaurSpecies = function (species) {
    const foundDinosaurs = [];

    for (const dinosaur of this.dinosaurs) {
        if (dinosaur.species === species) {
            foundDinosaurs.push(dinosaur);
        };
    };
    return foundDinosaurs
};

Park.prototype.calculateVisitorsPerDay = function () {
    let total = 0;

    for (const dinosaur of this.dinosaurs) {
        total += dinosaur.guestsAttractedPerDay;
    };
    return total;
};

Park.prototype.calculateVisitorsPerYear = function () {
    return this.calculateVisitorsPerDay() * 365;
};

Park.prototype.calculateRevenuePerYear = function () {
    return this.calculateVisitorsPerYear() * this.ticketPrice;
};

Park.prototype.removeAllDinosaursOfOneSpecies = function (species) {
    const newDinosaurList = [];

    for (const dinosaur of this.dinosaurs) {
        if (dinosaur.species !== species) {
            newDinosaurList.push(dinosaur);
        };
    };
    this.dinosaurs = newDinosaurList;
};

Park.prototype.dinosaurDietTypes = function () {
    const dietTypes = {}

    for (const dinosaur of this.dinosaurs) {
        if (dietTypes[dinosaur.diet]) {
            dietTypes[dinosaur.diet] += 1;
        }
        else {
            dietTypes[dinosaur.diet] = 1;
        };
    };
    return dietTypes;

};

module.exports = Park;