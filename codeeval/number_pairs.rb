require 'set'
File.open(ARGV[0]).each_line do |line|
    nums, x = line.split(";")
    nums, x = nums.split(",").map(&:to_i), x.to_i
    set = nums.to_set
    ans = nums.each.select {|i| x - i > i and set.member?(x - i)}
              .map {|i| "#{i},#{x - i}"}
    puts ans.size > 0 ? ans.join(";") : "NULL"
end
