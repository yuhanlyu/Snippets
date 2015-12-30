require 'scanf'
File.open(ARGV[0]).each_line do |line|
    line.scanf("Center: (%f, %f); Radius: %f; Point: (%f, %f)") {|cx,cy,r,x,y|
        puts ((cx-x).abs2 + (cy-y).abs2 <= r.abs2).to_s
    }
end
