#!/usr/bin/ruby

methods = ["mode", "ino", "dev", "nlink", "uid", "gid", "size", "atime", "mtime", "ctime"]

ARGV.each do |file|
  puts file
  statinfo=File::Stat.new(file)
  p statinfo
  methods.each do |meth|
    puts meth + " : " + statinfo.send(meth).to_s
  end
end
