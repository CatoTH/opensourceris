import List from "list.js";

export default class FacettedSearchFilterDropdown {
    constructor($facet) {
        this.$facet = $facet;
        this.$input = $facet.find(".value");
        this.$items = this.$facet.find(".filter-item");
        this.key = $facet.data("filter-key");

        this.filterlist = new List($facet[0], {
            valueNames: ['name'],
            listClass: 'filter-list',
            searchClass: 'filter-input'
        });
        this.filterlist.sort('name', {order: "asc"});
        this.$items.click(this.itemSelected.bind(this));
        this.setLabel();
        this.$facet.find(".remove-filter > a").click(this.removeFilter.bind(this));
    }

    setLabel() {
        let id = this.$input.val();
        if (id) {
            let name = this.$items.filter("[data-id=" + id + "]").find(".name").text();
            this.$facet.find(".nothing-selected").hide();
            this.$facet.find(".selection").show().text(name);

            this.$facet.find(".remove-filter").show();
        } else {
            this.$facet.find(".nothing-selected").show();
            this.$facet.find(".selection").hide().text("");

            this.$facet.find(".remove-filter").hide();
        }
    }

    itemSelected(ev) {
        let $item = $(ev.currentTarget),
            id = $item.data("id");
        this.$input.val(id).trigger("change");
        this.setLabel();
        ev.preventDefault();
    }

    getQueryString() {
        if (this.$input.val()) {
            return this.key + ":" + this.$input.val() + " ";
        } else {
            return '';
        }
    }

    removeFilter(event) {
        this.$input.val("").trigger("change");
        this.setLabel();
        event.preventDefault();
    }

    /**
     * Adds the item count to the values and hides away those with a count of zero. Also disables the button
     * when there is no value with a count biger than zero, unless a value is selected
     */
    update(data) {
        let $filter_list = $("#filter-" + this.key + "-list");
        let $button = $("#" + this.key + "Button");

        // Reset to defaults
        $button.prop("disabled", false);
        $filter_list.find(".filter-item").attr("hidden", "hidden");

        if (data['facets'][this.key].length === 0) {
            if (!this.$input.val()) {
                $button.prop("disabled", true);
            }
            return;
        }
        for (let bucket_entry of data['facets'][this.key]) {
            let $obj = $filter_list.find("[data-id=" + bucket_entry[0] + "]");
            $obj.find(".facet-item-count").text(" (" + bucket_entry[1] + ")");
            $obj.removeAttr("hidden");
        }
    }
}
