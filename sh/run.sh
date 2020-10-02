
# defining function
scriptFailed() {
    if [ "$run_status" -eq "1" ]; then
        echo "--> Failed fun, error caught"
    fi
}


python test.py
run_status=$?
echo "Success Status: $run_status"

scriptFailed

python deliberate_fail.py
run_status=$?
echo "Fail Status: $run_status"

scriptFailed
