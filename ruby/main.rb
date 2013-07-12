#!/usr/bin/ruby

def main()
    puts "hi, this is from inside main"
end

if __FILE__ == $0
    puts "about to call main"
    main()
    puts "just called main"
end
