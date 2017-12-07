Loan Repayment
==============

Bayesian approach to determining default risk for loans, using `Lending Club`_
data from 2007-2011. Follows along with some of the `Fast Forward Labs`_ guide
to probabilistic programming, but adding in my knowledge of ``pymc3`` following
presentations and tutorials for the library.


Data
----

The loan data from Lending Club contains the current status of the loan, the
loan principle, and attributes about the loan and the person getting the loan.
We want to limit ourselves to just those attributes that could be used by the
lendee to guage their own capability in repaying the loan, and to help them
decide if the loan is right for them.

Those columns are:

-   **annual_inc**: annual income of the lendee
-   **dti**: debt-to-income ratio, which is the ratio of monthly consumer debt
    payments (excluding mortgages) to monthly income
-   **revol_util**: credit card utilization as a fraction of available limit
-   **int_rate**: interest rate of the loan (in percent)
-   **loan_amnt**: amount of the loan in dollars
-   **term**: the length of time for the loan (either 3- or 5-year terms)
-   **purpose**: one of 14 categories from the lendee
-   **loan_status**: either "Fully Paid" or "Charged Off" (defaulted)
-   **total_rec_prncp**: value of the principle repaid

.. _`Lending Club`: https://www.lendingclub.com/info/download-data.action
.. _`Fast Forward Labs`: http://www.fastforwardlabs.com
