namespace Windows_form_app
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        String Cal_total, Option;
        int Num1, Num2, Res;

        private void Number1_Click(object sender, EventArgs e)
        {
            Txt_textbox.Text += Number1.Text;
        }

        private void Number2_Click(object sender, EventArgs e)
        {
            Txt_textbox.Text += Number2.Text;
        }

        private void Number3_Click(object sender, EventArgs e)
        {
            Txt_textbox.Text += Number3.Text;
        }

        private void Number4_Click(object sender, EventArgs e)
        {
            Txt_textbox.Text += Number4.Text;
        }

        private void Number5_Click(object sender, EventArgs e)
        {
            Txt_textbox.Text += Number5.Text;
        }

        private void Number6_Click(object sender, EventArgs e)
        {
            Txt_textbox.Text += Number6.Text;
        }

        private void Number7_Click(object sender, EventArgs e)
        {
            Txt_textbox.Text += Number7.Text;
        }

        private void Number8_Click(object sender, EventArgs e)
        {
            Txt_textbox.Text += Number8.Text;
        }

        private void Number9_Click(object sender, EventArgs e)
        {
            Txt_textbox.Text += Number9.Text;
        }

        private void Number10_Click(object sender, EventArgs e)
        {
            Txt_textbox.Text += Number10.Text;
        }

        private void Operator2_Click(object sender, EventArgs e)
        {
            Option = "-";

            Num1 = int.Parse(Txt_textbox.Text);

            Txt_textbox.Clear();
        }

        private void Operator3_Click(object sender, EventArgs e)
        {
            Option = "*";

            Num1 = int.Parse(Txt_textbox.Text);

            Txt_textbox.Clear();
        }

        private void Operator4_Click(object sender, EventArgs e)
        {
            Option = "/";

            Num1 = int.Parse(Txt_textbox.Text);

            Txt_textbox.Clear();
        }

        private void Operator1_Click(object sender, EventArgs e)
        {
            Option = "+";

            Num1 = int.Parse(Txt_textbox.Text);

            Txt_textbox.Clear();
        }

        private void Clear_data_Click(object sender, EventArgs e)
        {
            Txt_textbox.Clear();
            Res = (0);
            Num1 = (0);
            Num2 = (0);
        }

        private void Submitbtn_Click(object sender, EventArgs e)
        {
            Num2 = int.Parse(Txt_textbox.Text);

            if (Option == "+")
            {
                Res = Num1 + Num2;
            }
            else if (Option == "-")
            {
                Res = Num1 - Num2;
            }
            else if (Option == "*") {
                Res = Num1 * Num2;
            }
            else if (Option == "/") {
                Res = Num1 / Num2;
            }
            else{
                Console.Write( "!Error" );
            }

            Txt_textbox.Text = Res + "";
        }
    }
}
