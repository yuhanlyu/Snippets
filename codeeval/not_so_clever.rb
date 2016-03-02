File.open(ARGV[0]).each_line do |line|
    arr, n = line.chomp.split("|")
    arr, n = arr.split(" ").map(&:to_i), n.to_i
    n.times {
        (arr.size - 1).times { |i|
            if arr[i] > arr[i + 1]
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                break
            end
        }
    }
    puts arr.map(&:to_s).join(' ')    
end
