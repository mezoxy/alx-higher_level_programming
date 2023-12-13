#!/usr/bin/node

exports.esrever = function (list) {
  const holder = [];
  for (let i = 0; i < list.length; i++) {
    holder[i] = list[list.length - i - 1];
  }
  return (holder);
};
