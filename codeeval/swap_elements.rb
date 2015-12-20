File.open(ARGV[0]).each_line do |line|
    line = line.split(" : ")
    numbers = line[0].split
    line[1].split(", ").map {|x| x.split("-").map(&:to_i) }.each {|i, j|
        numbers[i], numbers[j] = numbers[j], numbers[i]
    }
    puts numbers.join(" ")
end
