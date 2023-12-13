#!/usr/bin/node

exports.converter = function (base) {
  return numToBase => numToBase.toString(base);
};
