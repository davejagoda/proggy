#!/usr/bin/ruby

require 'bundler/setup'
require 'rouge'

for arg in ARGV
  puts arg
  source = File.read(arg)
  formatter = Rouge::Formatters::HTML.new
  lexer = Rouge::Lexers::Shell.new
  puts 'HTML'
  puts formatter.format(lexer.lex(source))
  puts 'CSS'
  puts Rouge::Themes::Base16.mode(:light).render(scope: '.highlight')
end
