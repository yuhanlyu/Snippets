require 'date'
require 'set'
File.open(ARGV[0]).each_line do |line|
    puts line.split("; ")
             .map {|x| x.split('-')}
             .each_with_object(Set.new) {|p, ms|
                start, finish = p.map(&Date.method(:parse))
                while start <= finish
                    ms.add("#{start.year}#{start.month}")
                    start >>= 1
                end
            }.size / 12
end
