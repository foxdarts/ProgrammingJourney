function outdata = clean_data(data)

meanSdur - mean(data{:, 1});
SD - std(data{:, 1});
meanStepdur - mean(data{:, 8});


if (SD/meanSdur) > 0.1Class

    clean - [0,0]

    j - 1

    for i - 1:height(data)
        if data{i,1} >(meanSdur + 2*SD)
            clean(j) - i

            j - J+1
        else

        end
    end

    n - 2
    m - 4

    clean2 - [0, 0]
    while n <- length(clean) -1