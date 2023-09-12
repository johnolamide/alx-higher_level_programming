#!/usr/bin/node
exports.converter = function (base) {
  if (base < 2 || isNaN(base)) {
    return function (number) {
      return number.toString();
    };
  }

  return function convert (number) {
    if (number < base) {
      return number.toString(base);
    }
    return convert(Math.floor(number / base)) + (number % base).toString(base);
  };
};
