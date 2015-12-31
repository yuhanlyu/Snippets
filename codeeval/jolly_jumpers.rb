require 'set'
File.open(ARGV[0]).each_line do |line|
    n, *nums = line.split.map(&:to_i)
    puts nums.each_cons(2).map {|a,b| (a-b).abs}.to_set == (1..n - 1).to_set ?
            "Jolly" : "Not jolly"
end
