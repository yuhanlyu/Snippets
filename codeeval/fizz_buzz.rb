File.open(ARGV[0]).each_line do |line|
    x, y, n = line.split(" ").map(&:to_i)
    (1..n).each do |i|
        if i % x == 0
            print i % y == 0 ? "FB" : "F"
        else
            print i % y == 0 ? "B" : i
        end
        print " "
    end
    puts ""
end
