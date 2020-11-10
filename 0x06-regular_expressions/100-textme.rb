#!/usr/bin/env ruby
m = ARGV[0].scan(/\[from:(?<SENDER>.*?)\] .*\[to:(?<RECEIVER>.*?)\] .*\[flags:(?<FLAGS>.*?)\].*/).join(",")
puts m
