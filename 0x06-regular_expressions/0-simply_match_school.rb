#!/usr/bin/env ruby

def match_school(str)
  if str.match(/School/)
    puts "Match found!"
  else
    puts "Match not found."
  end
end

match_school(ARGV[0])
