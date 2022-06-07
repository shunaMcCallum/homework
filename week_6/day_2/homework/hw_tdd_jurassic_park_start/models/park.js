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
    const value = this.dinosaurs.reduce((max, obj) => (max.guestsAttractedPerDay > obj.guestsAttractedPerDay) ? max : obj);
    return value;
};


Park.prototype.findDinosaurSpecies = function (species) {
    let foundDinosaurs = [];
    for (let dinosaur of this.dinosaurs) {
        if (dinosaur.species === species) {
            foundDinosaurs.push(dinosaur);
        };
    };
    return foundDinosaurs
};

Park.prototype.calculateVisitorsPerDay = function () {
    let total = 0;
    for (let dinosaur of this.dinosaurs) {
        total += dinosaur.guestsAttractedPerDay;
    };
    return total;
};

Park.prototype.calculateVisitorsPerYear = function () {
    let visitorsPerDay = this.calculateVisitorsPerDay();
    let visitorsPerYear = visitorsPerDay * 365;
    return visitorsPerYear;
};

Park.prototype.calculateRevenuePerYear = function () {
    let visitorsPerYear = this.calculateVisitorsPerYear();
    let revenuePerYear = visitorsPerYear * this.ticketPrice;
    return revenuePerYear;
};

Park.prototype.removeAllDinosaursOfOneSpecies = function (species) {
    let newDinosaurList = [];
    for (let dinosaur of this.dinosaurs) {
        if (dinosaur.species !== species) {
            newDinosaurList.push(dinosaur);
        };
    };
    this.dinosaurs = newDinosaurList;
};

// Park.prototype.dinosaurDietTypes = function () {
//     const dietTypes = {}

//     for (let dinosaur of this.dinosaurs) {
//         let keys = Object.keys(dinosaur)
//         for (let key in keys) {
//             dietTypes[key] = 0;
//         };
//     };
//     return dietTypes;

// };

module.exports = Park;