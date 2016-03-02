File.open(ARGV[0]).each_line do |line|
    arr, result  = line.chomp.split(" ").map(&:to_i), 0
    gap = arr.size
    loop do
        gap, flag = [(gap / 1.25).floor, 1].max, false
        (arr.size - gap).times { |i|
            if arr[i] > arr[i + gap]
                flag = true
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
            end
        }
        if flag == false && gap == 1
            puts result
            break
        end
        result += 1
    end
end
